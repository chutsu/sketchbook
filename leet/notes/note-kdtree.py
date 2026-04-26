#!/usr/bin/env python3
"""
KD Tree
=======

A k-d tree is a space partitioning data structure for organizing points in a
k-dimensional space. The time complexity of constructing a k-d tree from N
points is:

- Python's timsort at every level of the k-d tree is O(N long N) time

- The construction recursively to the left and right subtrees, where each
  time the list of points is halved

    2 * O(0.5 N log 0.5 N)

  which is less than O(N long N), so therefore _at each level_ it is still
  O(N log N)

- Beacuse the list of points is halved at each level, there are O(log N)
  levels in the k-d tree

As a result the overall time complexity of constructing the k-d tree is
O(N(log N))^2.
"""
import numpy as np
from matplotlib.pylab import plt


def squared_euclidean_distance(x, y):
  """Compute the squared Euclidean distance between point x and y."""
  pt_a = np.array(x)
  pt_b = np.array(y)
  dx = pt_a[0] - pt_b[0]
  dy = pt_a[1] - pt_b[1]
  return dx * dx + dy * dy


def brute_force_nearest_neighbour(query_points, ref_points):
  """ Brute Force Nearest-Neighbour """
  neighbours = {}

  for query_pt in query_points:
    min_neighbour = ref_points[0]
    min_dist = squared_euclidean_distance(query_pt, ref_points[0])

    for ref_pt in ref_points[1:]:
      sed = squared_euclidean_distance(ref_pt, query_pt)
      if sed < min_dist:
        min_neighbour = ref_pt
        min_dist = sed

    neighbours[query_pt] = min_neighbour

  return neighbours


class Node:
  """ Binary Node """
  def __init__(self, point=None, left=None, right=None):
    self.point = point
    self.left = left
    self.right = right


class NearestNeighbour:
  """ Nearest Neighbour """
  def __init__(self, point=None, distance=None):
    self.point = point
    self.distance = distance

  def __str__(self):
    return f"point: {self.point}, distance: {self.distance}"


def _kdtree_build(k, points, depth):
  if len(points) == 0:
    return None

  points.sort(key=lambda x : x[depth % k])
  middle = int(len(points) / 2)

  return Node(
      point=points[middle],
      left=_kdtree_build(
          k,
          points[:middle],
          depth + 1,
      ),
      right=_kdtree_build(
          k,
          points[middle + 1:],
          depth + 1,
      ),
  )


def kdtree(points):
  """ Construct a k-d tree """
  k = len(points[0])
  return _kdtree_build(k, list(points), depth=0)


def kdtree_insert(tree, point, depth):
  k = len(point)
  axis = depth % k

  if tree is None:
    return Node(point)

  if point[axis] < tree.point[axis]:
    tree.left = kdtree_insert(tree, point, depth + 1)
  else:
    tree.right = kdtree_insert(tree, point, depth + 1)

  return tree


def _kdtree_search(k, node, point, depth, nn):
  if node is None:
    return

  # Keep track of nearest neighbour
  dist = squared_euclidean_distance(node.point, point)
  if dist < nn.distance:
    nn.point = node.point
    nn.distance = dist

  # Choose the next subtree to visit
  axis = depth % k
  next_node = None
  opposite_node = None
  if point[axis] < node.point[axis]:
    next_node = node.left
    opposite_node = node.right
  else:
    next_node = node.right
    opposite_node = node.left

  # Recursively search
  _kdtree_search(k, next_node, point, depth + 1, nn)

  # Check if the other subtree may contain a closer point
  if abs(point[axis] - node.point[axis]) < nn.distance:
    _kdtree_search(k, opposite_node, point, depth + 1, nn)


def find_nearest_neighbour_kdtree(root, point):
  """ Find the nearest neighbour in a k-d tree for a given point """
  k = len(point)
  depth = 0
  init_point = root.point
  init_dist = squared_euclidean_distance(root.point, point)
  nn = NearestNeighbour(init_point, init_dist)
  _kdtree_search(k, root, point, depth, nn)
  return nn.point


def print_tree(root):
  queue = [root]
  while len(queue):
    n = queue.pop(0)
    print(n.point)
    if n.left:
      queue.append(n.left)
    if n.right:
      queue.append(n.right)


if __name__ == "__main__":
  # x = (3, 4)
  # y = (4, 9)
  # squared_euclidean_distance(x, y)

  # Get the nearest neighbour from the query point's perspective
  # This approach uses a brute force method which is O(n^2) runtime
  # ref_points = [(1, 2), (3, 2), (4, 1), (3, 5)]
  # query_points = [(3, 4), (5, 1), (7, 3), (8, 9), (10, 1), (3, 3)]
  # neighbours = brute_force_nearest_neighbour(query_points, ref_points)
  # import pprint
  # pprint.pprint(neighbours)

  # Build KD Tree
  ref_points = [[1, 2], [3, 2], [4, 1], [3, 5]]
  query_points = [[3, 4], [5, 1], [7, 3], [8, 9], [10, 1], [3, 3]]
  tree = kdtree(ref_points)
  nn_point = find_nearest_neighbour_kdtree(tree, (8, 9))
  print(nn_point)

  # ref_points = np.array(ref_points)
  # query_points = np.array(query_points)
  # plt.plot(ref_points[:, 0], ref_points[:, 1], ".")
  # plt.plot(query_points[:, 0], query_points[:, 1], ".")
  # plt.show()
