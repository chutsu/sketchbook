#!/usr/bin/env python3
"""
Union Find
==========

Think of Union-Find (also known as a Disjoint Set Union or DSU) as a way to
keep track of "who belongs to which group" in a room full of people. It’s a
data structure that excels at handling two specific questions very quickly:

1. Union: Can you merge these two groups into one?
2. Find: Which group does this specific person belong to?

"""

class UnionFind:
  def __init__(self, n):
    self.parents = [i for i in range(n)]
    self.rank = [1] * n

  def find(self, x):
    if self.parents[x] != x:
      self.parents[x] = self.find(self.parents[x])
    return self.parents[x]

  def union(self, x, y):
    root1 = self.find(x)
    root2 = self.find(y)

    if root1 == root2:
      return 0

    if self.rank[root1] < self.rank[root2]:
      self.parents[root1] = root2
      self.rank[root2] += self.rank[root1]
    else:
      self.parents[root2] = root1
      self.rank[root1] += self.rank[root2]

    return 1


uf = UnionFind(9)

uf.union(0, 2)
uf.union(1, 4)
uf.union(1, 5)
uf.union(2, 3)
uf.union(2, 7)
uf.union(4, 8)
uf.union(5, 8)
