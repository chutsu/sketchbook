#!/usr/bin/env python3
"""
Segment Tree
============

Segment tree is a data structure used for storing information about intervals
or segments. It allows querying which of the stored segments contain a given
point. Segment trees can be used to solve:

- Range min / max
- Sum queries
- Range update queries

Segment trees only has three operations:

- Building the tree
- Updating the tree
- Querying the tree

In a segment tree, the array is stored at the leaves of the tree, while the
internal nodes store information about the segments represented by its children.
The internal nodes are formed in a bottom-up manner by merging the information
from its children nodes.

"""
import time
import random


class SegmentTree:
  def __init__(self, arr):
    self.n = len(arr)
    self.tree = [0] * self.n + arr
    for i in range(self.n - 1, 0, -1):
      self.tree[i] = self.tree[2 * i + 0] + self.tree[2 * i + 1]

  def update(self, i, value):
    i += self.n
    self.tree[i] = value

    while i > 1:
      i //= 2
      self.tree[i] = self.tree[2 * i + 0] + self.tree[2 * i + 1]

  def query(self, l, r):
    result = 0
    l += self.n
    r += self.n

    while l < r:
      if l % 2 == 1:
        result += self.tree[l]
        l += 1
      if r % 2 == 1:
        r -= 1
        result += self.tree[r]
      l //= 2
      r //= 2

    return result


if __name__ == "__main__":
  arr = [1, 3, 5, 7, 9, 11]

  stree = SegmentTree(arr)
  print(stree.query(0, 6))

  n = len(arr)
  for start in range(n):
    for end in range(n):
      assert stree.query(start, end) == sum(arr[start:end])
