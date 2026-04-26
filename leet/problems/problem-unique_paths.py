#!/usr/bin/env python3
# LeetCode 62: Unique Paths [Medium]


def dfs(m, n, i, j, results):
  if i < 0 or i >= m:
    return

  if j < 0 or j >= n:
    return

  if i == (m - 1) and j == (n - 1):
    results.append(1)
    return

  dfs(m, n, i + 1, j, results)
  dfs(m, n, i, j + 1, results)


def unique_paths(m, n):
  results = []
  i = 0
  j = 0
  dfs(m, n, i, j, results)
  return len(results)


if __name__ == "__main__":
  m = 3
  n = 7
  expected_result = 28
  result = unique_paths(m, n)
  assert(result == expected_result)
