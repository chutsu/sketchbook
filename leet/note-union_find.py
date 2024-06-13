#!/usr/bin/env python3
"""
Union Find
==========

Union Find is a data structure that stores non-overlapping or disjoint subset
of elements, it is also called a disjoint set data structure.

"""

class UnionFind:
  def __init__(self, N):
    self.parents = list(range(N))

  def union(self, parent, child):
    self.parents[self.find(child)] = self.find(parent)

  def find(self, x):
    if x != self.parents[x]:
      self.parents[x] = self.find(self.parents[x])
    return self.parents[x]


class UnionFind2:
  def __init__(self, N):
    self.parents = list(range(N))
    self.rank = [1] * N

  def find(self, x):
    if x != self.parents[x]:
      self.parents[x] = self.find(self.parents[x])
    return self.parents[x]

  def union(self, parent, child):
    root1 = self.find(parent)
    root2 = self.find(child)

    if root1 == root2:
      return

    if self.rank[root1] > self.rank[root2]:
      self.parents[root2] = root1
    if self.rank[root1] < self.rank[root2]:
      self.parents[root1] = root2
    else:
      self.parents[root2] = root1
      self.rank[root1] += 1


uf = UnionFind2(9)

uf.union(0, 2)
uf.union(1, 4)
uf.union(1, 5)
uf.union(2, 3)
uf.union(2, 7)
uf.union(4, 8)
uf.union(5, 8)

print(uf.parents)
print(uf.rank)
