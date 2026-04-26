#!/usr/bin/env python3
"""
Kruskals Algorithm
==================

Kruskal’s is a greedy algorithm used to find the Minimum Spanning Tree (MST) of
a weighted graph. In plain English: it finds the cheapest way to connect all
"nodes" (like cities or servers) without creating any loops.

"""

class UnionFind:
  def __init__(self, n):
    self.parent = list(range(n))
    self.rank = [0] * n

  def find(self, i):
    if self.parent[i] != i:
      self.parent[i] = self.find(self.parent[i])
    return self.parent[i]

  def union(self, i, j):
    root_i = self.find(i)
    root_j = self.find(j)

    if root_i == root_j:
      return False

    if self.rank[root_i] < self.rank[root_j]:
      self.parent[root_i] = root_j
      self.rank[root_j] += self.rank[root_i]
    else:
      self.parent[root_j] = root_i
      self.rank[root_i] += self.rank[root_j]

    return True


def kruskals(num_nodes, edges):
  # Edges is a list of [u, v, weight]
  # 1. Sort edges by weight
  edges.sort(key=lambda x: x[2])

  uf = UnionFind(num_nodes)
  mst_weight = 0
  mst_edges = []

  for u, v, weight in edges:
    if uf.union(u, v):
      mst_weight += weight
      mst_edges.append((u, v, weight))

  return mst_weight, mst_edges
