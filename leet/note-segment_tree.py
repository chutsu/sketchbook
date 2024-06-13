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

https://codeforces.com/blog/entry/18051

"""
import time
import random


class SegmentTree:
  def __init__(self, arr):
    self.N = len(arr)
    self.data = [0] * (2 * N)
    self.data[N:] = arr
    for i in range(N - 1, 0, -1):
      self.data[i] = self.data[2 * i] + self.data[2 * i + 1]

  def query(self, l, r):
    res = 0
    l += self.N
    r += self.N

    while l < r:
      if l % 2 == 1:
        res += self.data[l]
        l += 1

      if r % 2 == 1:
        r -= 1
        res += self.data[r]

      l = l // 2
      r = r // 2

    return res

  def modify(self, i, value):
    i += self.N
    self.data[i] = value

    while i > 1:
      i = i // 2
      self.data[i] = self.data[2 * i] + self.data[2 * i + 1]


if __name__ == "__main__":
  N = 10
  arr = [x for x in range(N)]

  tree = SegmentTree(arr)
  s = 0
  e = N
  print(tree.data)
  print(tree.query(s, e))
  print(sum(arr[s:e]))
  assert tree.query(s, e) == sum(arr[s:e])

  index = random.randint(0, N - 1)
  value = random.randint(0, N - 1)
  tree.modify(index, value)
  arr[index] = value
  print(tree.data)
  print(tree.query(s, e))
  print(sum(arr[s:e]))
  assert tree.query(s, e) == sum(arr[s:e])
