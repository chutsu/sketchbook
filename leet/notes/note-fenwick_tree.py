#!/usr/bin/env python3
"""
A Fenwick Tree, also known as a Binary Indexed Tree (BIT), is a data structure
that provides efficient methods for cumulative frequency tables. It allows both
point updates and prefix sum queries to be performed in O(log n) time, where n
is the number of elements in the array. This efficiency makes Fenwick Trees
particularly useful for problems involving cumulative frequency tables and
dynamic cumulative sums.

Reference:
https://www.youtube.com/watch?v=CWDQJGaN1gY
"""


class FenwickTree:
  def __init__(self, n):
    self.size = n
    self.tree = [0] * (n + 1)

  def update(self, i, delta):
    i += 1
    while i <= self.size:
      self.tree[i] += delta
      i += i & (-i)

  def query(self, i):
    i += 1
    s = 0
    while i > 0:
      s += self.tree[i]
      i -= i & (-i)
    return s

  def range_query(self, left, right):
    return self.query(right) - self.query(left - 1)

arr = [5, 2, 9, -3, 5, 20, 10, -7]
ftree = FenwickTree(8)
for i, val in enumerate(arr):
  ftree.update(i, val)

print(arr)
print(ftree.tree)
print(ftree.query(1))
print(ftree.query(2))
print(ftree.range_query(1, 2))
