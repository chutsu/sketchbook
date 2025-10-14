#!/usr/bin/env python3
from pathlib import Path
import typing
from typing import TypeVar
from typing import Annotated
from typing import Literal

from math import cos
from math import sin

import rerun as rr
import numpy as np
import scipy
import open3d as o3d


from numpy.typing import NDArray

DType = TypeVar("DType", bound=np.generic)
Vec2 = Annotated[NDArray[DType], Literal[2]]
Vec3 = Annotated[NDArray[DType], Literal[3]]
Vec4 = Annotated[NDArray[DType], Literal[4]]
Vec5 = Annotated[NDArray[DType], Literal[5]]
Vec6 = Annotated[NDArray[DType], Literal[6]]
Vec7 = Annotated[NDArray[DType], Literal[7]]
VecN = Annotated[NDArray[DType], Literal["N"]]
Mat2 = Annotated[NDArray[DType], Literal[2, 2]]
Mat3 = Annotated[NDArray[DType], Literal[3, 3]]
Mat34 = Annotated[NDArray[DType], Literal[3, 4]]
Mat4 = Annotated[NDArray[DType], Literal[4, 4]]
MatN = Annotated[NDArray[DType], Literal["N", "N"]]
MatNx2 = Annotated[NDArray[DType], Literal["N", "2"]]
MatNx3 = Annotated[NDArray[DType], Literal["N", "3"]]
MatNx4 = Annotated[NDArray[DType], Literal["N", "4"]]
Mat2xN = Annotated[NDArray[DType], Literal["2", "N"]]
Mat2x3 = Annotated[NDArray[DType], Literal["2", "3"]]
Mat3x4 = Annotated[NDArray[DType], Literal["3", "4"]]
Mat3xN = Annotated[NDArray[DType], Literal["3", "N"]]
Mat4xN = Annotated[NDArray[DType], Literal["4", "N"]]
Image = Annotated[NDArray[DType], Literal["N", "N"]]


def euler321(
    yaw: float | np.float32 | np.float64,
    pitch: float | np.float32 | np.float64,
    roll: float | np.float32 | np.float64,
) -> Mat3:
    """
    Convert yaw, pitch, roll in radians to a 3x3 rotation matrix.

    Source:
    Kuipers, Jack B. Quaternions and Rotation Sequences: A Primer with
    Applications to Orbits, Aerospace, and Virtual Reality. Princeton, N.J:
    Princeton University Press, 1999. Print.
    [Page 85-86, "The Aerospace Sequence"]
    """
    psi = yaw
    theta = pitch
    phi = roll

    cpsi = cos(psi)
    spsi = sin(psi)
    ctheta = cos(theta)
    stheta = sin(theta)
    cphi = cos(phi)
    sphi = sin(phi)

    C11 = cpsi * ctheta
    C21 = spsi * ctheta
    C31 = -stheta

    C12 = cpsi * stheta * sphi - spsi * cphi
    C22 = spsi * stheta * sphi + cpsi * cphi
    C32 = ctheta * sphi

    C13 = cpsi * stheta * cphi + spsi * sphi
    C23 = spsi * stheta * cphi - cpsi * sphi
    C33 = ctheta * cphi

    return np.array([[C11, C12, C13], [C21, C22, C23], [C31, C32, C33]])


def hat(vec: Vec3) -> Mat3:
    """Form skew-symmetric matrix from vector `vec`"""
    assert vec.shape == (3,) or vec.shape == (3, 1)

    if vec.shape == (3,):
        x = vec[0]
        y = vec[1]
        z = vec[2]
    else:
        x = vec[0][0]
        y = vec[1][0]
        z = vec[2][0]

    return np.array([[0.0, -z, y], [z, 0.0, -x], [-y, x, 0.0]])


def Exp(phi: Vec3) -> Mat3:
    """Exponential Map"""
    assert phi.shape == (3,) or phi.shape == (3, 1)
    if np.linalg.norm(phi) < 1e-3:
        C = np.eye(3) + hat(phi)
        return C

    phi_norm = np.linalg.norm(phi)
    phi_skew = hat(phi)
    phi_skew_sq = phi_skew @ phi_skew

    C = np.eye(3)
    C += (np.sin(phi_norm) / phi_norm) * phi_skew
    C += ((1 - np.cos(phi_norm)) / phi_norm**2) * phi_skew_sq
    return C


def quat_norm(q: Vec4) -> float:
    """Returns norm of a quaternion"""
    qw, qx, qy, qz = q
    return np.sqrt(qw**2 + qx**2 + qy**2 + qz**2)


def quat_normalize(q: Vec4) -> Vec4:
    """Normalize quaternion"""
    n = quat_norm(q)
    qw, qx, qy, qz = q
    return np.array([qw / n, qx / n, qy / n, qz / n])


def quat_left(q: Vec4) -> Mat4:
    """Quaternion left product matrix"""
    qw, qx, qy, qz = q
    row0 = [qw, -qx, -qy, -qz]
    row1 = [qx, qw, -qz, qy]
    row2 = [qy, qz, qw, -qx]
    row3 = [qz, -qy, qx, qw]
    return np.array([row0, row1, row2, row3])


def quat_right(q: Vec4) -> Mat4:
    """Quaternion right product matrix"""
    qw, qx, qy, qz = q
    row0 = [qw, -qx, -qy, -qz]
    row1 = [qx, qw, qz, -qy]
    row2 = [qy, -qz, qw, qx]
    row3 = [qz, qy, -qx, qw]
    return np.array([row0, row1, row2, row3])


def quat_lmul(p: Vec4, q: Vec4) -> Vec4:
    """Quaternion left multiply"""
    assert len(p) == 4
    assert len(q) == 4
    lprod = quat_left(p)
    return lprod @ q


def quat_rmul(p: Vec4, q: Vec4) -> Vec4:
    """Quaternion right multiply"""
    assert len(p) == 4
    assert len(q) == 4
    rprod = quat_right(q)
    return rprod @ p


def quat_delta(dalpha: Vec3) -> Vec4:
    """Form quaternion from small angle rotation vector dalpha"""
    half_norm = 0.5 * np.linalg.norm(dalpha)
    scalar = np.cos(half_norm)
    vector = np.sinc(half_norm) * 0.5 * dalpha

    dqw = scalar
    dqx, dqy, dqz = vector
    dq = np.array([dqw, dqx, dqy, dqz])

    return dq


def rot2quat(C: Mat3) -> Vec4:
    """
    Convert 3x3 rotation matrix to quaternion.
    """
    assert C.shape == (3, 3)

    m00 = C[0, 0]
    m01 = C[0, 1]
    m02 = C[0, 2]

    m10 = C[1, 0]
    m11 = C[1, 1]
    m12 = C[1, 2]

    m20 = C[2, 0]
    m21 = C[2, 1]
    m22 = C[2, 2]

    tr = m00 + m11 + m22

    if tr > 0:
        S = np.sqrt(tr + 1.0) * 2.0
        # S=4*qw
        qw = 0.25 * S
        qx = (m21 - m12) / S
        qy = (m02 - m20) / S
        qz = (m10 - m01) / S
    elif (m00 > m11) and (m00 > m22):
        S = np.sqrt(1.0 + m00 - m11 - m22) * 2.0
        # S=4*qx
        qw = (m21 - m12) / S
        qx = 0.25 * S
        qy = (m01 + m10) / S
        qz = (m02 + m20) / S
    elif m11 > m22:
        S = np.sqrt(1.0 + m11 - m00 - m22) * 2.0
        # S=4*qy
        qw = (m02 - m20) / S
        qx = (m01 + m10) / S
        qy = 0.25 * S
        qz = (m12 + m21) / S
    else:
        S = np.sqrt(1.0 + m22 - m00 - m11) * 2.0
        # S=4*qz
        qw = (m10 - m01) / S
        qx = (m02 + m20) / S
        qy = (m12 + m21) / S
        qz = 0.25 * S

    return quat_normalize(np.array([qw, qx, qy, qz]))


def quat_mul(p: Vec4, q: Vec4) -> Vec4:
    """Quaternion multiply p * q"""
    return quat_lmul(p, q)


def quat2rot(q: Vec4) -> Mat3:
    """
    Convert quaternion to 3x3 rotation matrix.

    Source:
    Blanco, Jose-Luis. "A tutorial on se (3) transformation parameterizations
    and on-manifold optimization." University of Malaga, Tech. Rep 3 (2010): 6.
    [Page 18, Equation (2.20)]
    """
    assert len(q) == 4
    qw, qx, qy, qz = q

    qx2 = qx**2
    qy2 = qy**2
    qz2 = qz**2
    qw2 = qw**2

    # Homogeneous form
    C11 = qw2 + qx2 - qy2 - qz2
    C12 = 2.0 * (qx * qy - qw * qz)
    C13 = 2.0 * (qx * qz + qw * qy)

    C21 = 2.0 * (qx * qy + qw * qz)
    C22 = qw2 - qx2 + qy2 - qz2
    C23 = 2.0 * (qy * qz - qw * qx)

    C31 = 2.0 * (qx * qz - qw * qy)
    C32 = 2.0 * (qy * qz + qw * qx)
    C33 = qw2 - qx2 - qy2 + qz2

    return np.array([[C11, C12, C13], [C21, C22, C23], [C31, C32, C33]])


class BunnyData:
    def __init__(self, data_dir: Path):
        self.data_dir = data_dir
        self.pcd_files = sorted([x for x in Path("data/bunny").glob("*.xyz")])
        self.pose_files = sorted([x for x in Path("data/bunny").glob("*.txt")])
        self.length = len(self.pcd_files)
        assert len(self.pcd_files) == len(self.pose_files)

    def load_scan(self, index):
        assert index < self.length
        return np.genfromtxt(self.pcd_files[index], delimiter=" ")

    def load_pose(self, index):
        assert index < self.length
        return np.genfromtxt(self.pose_files[index])


class Frame:
    def __init__(self, pcd, prev_frame=None):
        self.T = np.eye(4)
        self.pcd = pcd
        self.prev_frame = prev_frame

    def points(self):
        R = self.T[:3, :3]
        t = self.T[:3, 3]
        return (R @ self.pcd[:, :3].T).T + t

    def estimate(self, frame_kp1):
        pcd_src = o3d.geometry.PointCloud()
        pcd_dst = o3d.geometry.PointCloud()

        src_points = [self.points()]
        prev_frame = self.prev_frame
        num_prev_frames = 0
        while prev_frame is not None:
            src_points.append(prev_frame.points())
            prev_frame = prev_frame.prev_frame
            num_prev_frames += 1
            # if num_prev_frames >= 10:
            #   break
        src_points = np.vstack(src_points)

        pcd_src.points = o3d.utility.Vector3dVector(src_points)
        pcd_dst.points = o3d.utility.Vector3dVector(frame_kp1.points())

        threshold = 10000
        trans_init = np.linalg.inv(self.T)
        result = o3d.pipelines.registration.registration_icp(
            pcd_src,
            pcd_dst,
            threshold,
            trans_init,
            o3d.pipelines.registration.TransformationEstimationPointToPoint(),
            o3d.pipelines.registration.ICPConvergenceCriteria(
                relative_fitness=1e-12,
                relative_rmse=1e-12,
                max_iteration=20000,
            ),
        )
        R_est = result.transformation[0:3, 0:3]
        t_est = result.transformation[0:3, 3]
        print(f"{result.inlier_rmse=}")
        print(f"{result.fitness=}")
        print("")

        frame_kp1.T = np.eye(4)
        frame_kp1.T[0:3, 0:3] = R_est.T
        frame_kp1.T[0:3, 3] = -R_est.T @ t_est
        return frame_kp1


def icp_open3d(src_points, dst_points):
    pcd_src = o3d.geometry.PointCloud()
    pcd_dst = o3d.geometry.PointCloud()
    pcd_src.points = o3d.utility.Vector3dVector(src_points)
    pcd_dst.points = o3d.utility.Vector3dVector(dst_points)
    threshold = 1000
    trans_init = np.eye(4)
    result = o3d.pipelines.registration.registration_icp(
        pcd_src,
        pcd_dst,
        threshold,
        trans_init,
        o3d.pipelines.registration.TransformationEstimationPointToPoint(),
        o3d.pipelines.registration.ICPConvergenceCriteria(max_iteration=20000),
    )
    # pcd_src_icp = pcd_src.transform(result.transformation)

    R_est = result.transformation[0:3, 0:3]
    t_est = result.transformation[0:3, 3]
    # dst_points_est = (R_est @ src_points.T).T + t_est

    # rr.log("src-points", rr.Points3D(src_points, colors=[1.0, 0.0, 0.0], radii=0.0001))
    # rr.log("dst-points", rr.Points3D(dst_points, colors=[0.0, 1.0, 0.0], radii=0.0001))
    # rr.log(
    #     "dst_est-points",
    #     rr.Points3D(dst_points_est, colors=[0.0, 0.0, 1.0], radii=0.0001),
    # )

    return R_est, t_est


def umeyama(X: MatNx3, Y: MatNx3) -> tuple[float, Mat3, Vec3]:
    """
    Estimates scale `c`, rotation matrix `R` and translation vector `t` between
    two sets of points `X` and `Y` such that:

      Y ~= c * R @ X + t

    Args:

      X: src 3D points
      Y: dest 3D points

    Returns:

      c: Scale factor
      R: Rotation matrix
      t: translation vector

    """
    # Compute centroid
    mu_x = X.mean(axis=1).reshape(-1, 1)
    mu_y = Y.mean(axis=1).reshape(-1, 1)

    # Form covariance matrix and decompose with SVD
    var_x = np.square(X - mu_x).sum(axis=0).mean()
    cov_xy = ((Y - mu_y) @ (X - mu_x).T) / X.shape[1]
    U, D, VH = np.linalg.svd(cov_xy)

    # Check to see if rotation matrix det(R) is 1
    S = np.eye(X.shape[0])
    if np.linalg.det(U) * np.linalg.det(VH) < 0:
        S[-1, -1] = -1

    # Calculate scale, rotation matrix and translation vector
    c = np.trace(np.diag(D) @ S) / var_x
    R = U @ S @ VH
    t = mu_y - c * R @ mu_x

    return c, R, t


if __name__ == "__main__":
    rr.init("icp", spawn=True)

    data = BunnyData(Path("data/bunny"))

    frames = []
    radii = 0.0001
    red = [1.0, 0.0, 0.0]
    green = [0.0, 1.0, 0.0]
    blue = [0.0, 0.0, 1.0]
    for i in range(20):
        if i == 0:
            scan = data.load_scan(i)
            frames.append(Frame(scan))
        else:
            prev_frame = frames[i - 1]
            scan = data.load_scan(i)
            frames.append(Frame(scan, prev_frame))

        if i >= 1:
            frame_km1 = frames[i - 1]
            frame_k = frames[i]
            frame_km1.estimate(frame_k)

            points_km1 = frame_km1.points()
            points_k = frame_k.points()

            rr.set_time("iteration", sequence=i)
            rr.log("src-points", rr.Points3D(points_km1, colors=blue, radii=radii))
            rr.log("dst-points", rr.Points3D(points_k, colors=green, radii=radii))
            rr.log("points", rr.Points3D(points_k, colors=red, radii=radii))

    # frame0 = Frame(data.load_scan(0))
    # frame1 = Frame(data.load_scan(1))
    # frame2 = Frame(data.load_scan(2))
    # frame3 = Frame(data.load_scan(3))

    # frame0.estimate(frame1)
    # frame1.estimate(frame2)
    # frame2.estimate(frame3)
    #
    # radii = 0.0001
    # red = [1.0, 0.0, 0.0]
    # green = [0.0, 1.0, 0.0]
    # blue = [0.0, 0.0, 1.0]
    # rr.set_time("iteration", sequence=0)
    # rr.log("points", rr.Points3D(frame0.points(), colors=red, radii=radii))
    # rr.set_time("iteration", sequence=1)
    # rr.log("points", rr.Points3D(frame1.points(), colors=green, radii=radii))
    # rr.set_time("iteration", sequence=2)
    # rr.log("points", rr.Points3D(frame2.points(), colors=blue, radii=radii))
    # rr.set_time("iteration", sequence=3)
    # rr.log("points", rr.Points3D(frame3.points(), colors=blue, radii=radii))

    # src_points = frame0.points()
    # dst_points = frame1.points()
    # icp_open3d(src_points, dst_points)

    # max_iter = 50
    # tree = scipy.spatial.KDTree(src_points)
    # R_est = np.eye(3)
    # # R_est = euler321(0.1, 0.2, 0.0)
    # t_est = np.array([0.0, 0.0, 1.0])
    #
    # for i in range(max_iter):
    #     dst_points_est = (R_est @ src_points.T).T + t_est
    #
    #     radii = 0.0001
    #     red = [1.0, 0.0, 0.0]
    #     green = [0.0, 1.0, 0.0]
    #     blue = [0.0, 0.0, 1.0]
    #     rr.set_time("iteration", sequence=i)
    #     rr.log("src-points", rr.Points3D(src_points, colors=red, radii=radii))
    #     rr.log("dst-points", rr.Points3D(dst_points, colors=green, radii=radii))
    #     rr.log("dst_est-points", rr.Points3D(dst_points_est, colors=blue, radii=radii))
    #
    #     distances, indicies = tree.query(dst_points_est)
    #     threshold = np.std(distances) * 2.0
    #     distances = distances.tolist()
    #
    #     gnd = []
    #     est = []
    #     for i, index in enumerate(indicies):
    #         if threshold < distances[i]:
    #             gnd.append(dst_points[index])
    #             est.append(dst_points_est[i])
    #     N = len(gnd)
    #     gnd = np.array(gnd)
    #     est = np.array(est)
    #
    #     jacobians = []
    #     residuals = []
    #     for i in range(N):
    #         residuals.append(gnd[i] - est[i])
    #         J = np.zeros((3, 6))
    #         J[0:3, 0:3] = -1.0 * np.eye(3)
    #         J[0:3, 3:6] = R_est @ hat(est[i])
    #         jacobians.append(J)
    #     J = np.vstack(jacobians)
    #     r = np.hstack(residuals)
    #     cost = 0.5 * (r.T @ r)
    #     print(f"{cost=:.2e}")
    #
    #     H = J.T @ J
    #     H += 1e4 * np.eye(6)
    #     b = -1.0 * J.T @ r
    #
    #     c, low = scipy.linalg.cho_factor(H)
    #     dx = scipy.linalg.cho_solve((c, low), b)
    #
    #     t_est += dx[0:3]
    #     # R_est = R_est @ Exp(dx[3:6])
    #
    #     q_est = rot2quat(R_est)
    #     dq = quat_delta(dx[3:6])
    #     q_new = quat_mul(q_est, dq)
    #     q_new = quat_normalize(q_new)
    #     R_est = quat2rot(q_new)
