#!/usr/bin/env python3
import scipy
import numpy as np
from numpy import eye
from numpy import zeros
import matplotlib.pyplot as plt

from xyz import hat
from xyz import euler321
from xyz import Exp
from xyz import solve_svd
from xyz import rot_diff
from xyz import plot_set_axes_equal


def umeyama(X, Y):
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
  S = eye(X.shape[0])
  if np.linalg.det(U) * np.linalg.det(VH) < 0:
    S[-1, -1] = -1

  # Calculate scale, rotation matrix and translation vector
  c = np.trace(np.diag(D) @ S) / var_x
  R = U @ S @ VH
  t = mu_y - c * R @ mu_x

  return c, R, t


def icp(X, Y, **kwargs):
  # Parameters
  prev_error = float("inf")
  max_iter = kwargs.get("max_iter", 2)
  tol = kwargs.get("tol", 1e-8)

  # Setup
  R = None
  t = None

  # -- Setup plotting
  plt.figure(figsize=(12, 10))
  ax = plt.axes(projection="3d")
  ax.scatter(X[:, 0], X[:, 1], X[:, 2], color="r", label="src", alpha=0.2)
  ax.scatter(Y[:, 0], Y[:, 1], Y[:, 2], color="g", label="dest", alpha=0.2)
  plt.legend(loc=0)
  # plt.show()

  # Optimize
  est_ax = None
  for _ in range(max_iter):
    # Step 1: Find closest points in Y for each point in X
    tree = scipy.spatial.KDTree(Y)
    distances, indices = tree.query(X)
    closest_Y = Y[indices]

    # Step 2: Compute transformation using Least Squares
    _, R, t = umeyama(X.T, closest_Y.T)

    # Step 3: Apply transformation
    X = (X @ R.T) + t.T

    # Plot
    if est_ax:
      est_ax.remove()
    est_ax = ax.scatter(X[:, 0],
                        X[:, 1],
                        X[:, 2],
                        color="k",
                        label="est",
                        alpha=0.2)
    plot_set_axes_equal(ax)
    plt.draw()
    plt.pause(0.5)
    # plt.show()

    # Step 4: Check for convergence
    mean_error = np.mean(distances)
    if abs(prev_error - mean_error) < tol:
      break
    prev_error = mean_error

  return X, R, t


def test_umeyama():
    R_gnd = euler321(*np.random.rand(3))
    t_gnd = np.random.rand(3, 1) * 0.1

    points = np.random.rand(int(1e7), 3)
    src = points
    dst = points @ R_gnd.T + t_gnd.T
    c, R, t = umeyama(src.T, dst.T)
    est = c * src @ R.T + t.T

    assert np.allclose(R, R_gnd, atol=1e-4)
    assert np.allclose(t, t_gnd, atol=1e-4)
    assert np.allclose(est, dst, atol=1e-4)


def test_icp():
    R_gnd = euler321(*np.random.rand(3))
    t_gnd = np.random.rand(3) * 2

    R_est = R_gnd @ euler321(*np.random.rand(3) * 0.2)
    t_est = t_gnd + np.random.rand(3)

    N = 10000
    p_src = np.random.rand(3, N)
    p_dst_gnd = (R_gnd @ p_src) + t_gnd[:, np.newaxis]

    max_iter = 10
    for _ in range(max_iter):
        p_dst_est = (R_est @ p_src) + t_est[:, np.newaxis]

        jacobians = []
        residuals = []
        for i in range(N):
            residuals.append(p_dst_gnd[:, i] - p_dst_est[:, i])
            J = zeros((3, 6))
            J[0:3, 0:3] = -1.0 * eye(3)
            J[0:3, 3:6] = R_est @ hat(p_dst_est[:, i])
            jacobians.append(J)
        J = np.vstack(jacobians)
        r = np.hstack(residuals)

        H = J.T @ J
        H += 1e-4 * eye(6)
        b = -1.0 * J.T @ r
        dx = solve_svd(H, b)

        t_est += dx[0:3]
        R_est = R_est @ Exp(dx[3:6])

    assert np.linalg.norm(t_est - t_gnd) < 1e-2
    assert rot_diff(R_est, R_gnd) < 1e-2
