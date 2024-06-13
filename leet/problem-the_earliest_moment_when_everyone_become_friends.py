#!/usr/bin/env python3
"""
LeetCode 1101: The Earliest Moment When Everyone Become Friends

There are n people in a social group labeled from 0 to n - 1. You are
given an array logs where logs[i] = [timestampi, xi, yi] indicates that
xi and yi will be friends at the time timestampi.

Friendship is symmetric. That means if a is friends with b, then b is
friends with a. Also, person a is acquainted with a person b if a is
friends with b, or a is a friend of someone acquainted with b.

Return the earliest time for which every person became acquainted with
every other person. If there is no such earliest time, return -1.
"""


class UnionFind:
  def __init__(self, n):
    self.group = [i for i in range(n)]
    self.rank = [0 for _ in range(n)]

  def find(self, x):
    if self.group[x] != x:
      self.group[x] = self.find(self.group[x])
    return self.group[x]

  def union(self, x, y):
    group_a = self.find(x)
    group_b = self.find(y)
    if group_a == group_b:
      return False

    if self.rank[group_a] > self.rank[group_b]:
      self.group[group_b] = group_a
    elif self.rank[group_a] < self.rank[group_b]:
      self.group[group_a] = group_b
    else:
      self.group[group_a] = group_b
      self.rank[group_b] += 1

    return True


def find_moment(logs, n):
  uf = UnionFind(n)

  num_groups = n
  for timestamp, x, y in logs:
    if uf.union(x, y):
      num_groups -= 1

    if num_groups == 1:
      return timestamp

  return None


if __name__ == "__main__":
  logs = [
      [20190101, 0, 1],
      [20190104, 3, 4],
      [20190107, 2, 3],
      [20190211, 1, 5],
      [20190224, 2, 4],
      [20190301, 0, 3],
      [20190312, 1, 2],
      [20190322, 4, 5],
  ]
  n = 6
  expected = 20190301
  assert find_moment(logs, n) == expected
