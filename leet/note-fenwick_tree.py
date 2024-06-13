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

def update(ftree, index, value):
  while index < len(ftree):
    ftree[index] += value
    index += index & -index


def build(array):
  n = len(array)
  ftree = [0] * n
  for i in range(1, n):
    update(ftree, i, array[i])
  return ftree


def get_sum(ftree, index):
  ans = 0
  while index > 0:
    ans += ftree[index]
    index -= index & -index
  return ans


def get_range_sum(ftree, left, right):
  ans = get_sum(ftree, right) - get_sum(ftree, left - 1)
  return ans


arr = [x for x in range(10)]
ftree = build(arr)
print(ftree)
print(get_sum(ftree, 5))
print(get_range_sum(ftree, 0, 5))
