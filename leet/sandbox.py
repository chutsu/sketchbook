import heapq
from collections import defaultdict
import numpy as np


class UnionFind:
  def __init__(self, N):
    self.parents = [i for i in range(N)]
    self.rank = [1 for _ in range(N)]

  def find(self, x):
    if x != self.parents[x]:
      self.parents[x] = self.find(self.parents[x])
    return self.parents[x]


  def union(self, x, y):
    root1 = self.find(x)
    root2 = self.find(y)

    if root1 == root2:
      return False

    if self.rank[root1] > self.rank[root2]:
      self.parents[root2] = root1
      self.rank[root1] += self.rank[root2]
    else:
      self.parents[root1] = root2
      self.rank[root2] += self.rank[root1]

    return True


def kahn(graph, n):
  adjlist = defaultdict(list)
  indegrees = defaultdict(int)
  for prereq, src in graph:
    adjlist[prereq].append(src)
    indegrees[src] += 1

  q = []
  for i in range(num_nodes):
    if indegrees[i] == 0:
      q.append(i)

  topo = []
  while q:
    u = q.pop(0)
    topo.append(u)

    for v in adjlist[u]:
      indegrees[v] -= 1
      if indegrees[v] == 0:
        q.append(v)

  if len(topo) == n:
    return topo[::-1]

  return []


class Node:
  def __init__(self, point, axis, left=None, right=None):
    self.point = point
    self.axis = axis
    self.left = left
    self.right = right


def kdtree_build(k, points, depth):
  if len(points) == 0:
    return None

  axis = depth % k
  points.sort(key=lambda x: x[axis])
  middle = len(points) // 2

  return Node(
    point=points[middle],
    axis=axis,
    left=kdtree_build(k, points[:middle], depth + 1),
    right=kdtree_build(k, points[middle+1:], depth + 1),
  )


class NearestNeighbour:
  def __init__(self, point, distance):
    self.point = point
    self.distance = distance

def squared_euclidean_distance(x, y):
  """Compute the squared Euclidean distance between point x and y."""
  pt_a = np.array(x)
  pt_b = np.array(y)
  dx = pt_a[0] - pt_b[0]
  dy = pt_a[1] - pt_b[1]
  return dx * dx + dy * dy


def kdtree_search(k, node, point, nn):
  if node is None:
    return

  dist = squared_euclidean_distance(node.point, point)
  if dist < nn.distance:
    nn.point = node.point
    nn.dist = dist

  axis = node.axis
  next_node = None
  opposite_node = None
  if point[axis] < node.point[axis]:
    next_node = node.left
    opposite_node = node.right
  else:
    next_node = node.right
    opposite_node = node.left

  kdtree_search(k, next_node, point, nn)
  if (point[axis] - node.point[axis])**2 < nn.distance:
    kdtree_search(k, opposite_node, point, nn)


num_nodes = 5
dependencies = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]
topo = kahn(dependencies, num_nodes)
print(topo)
