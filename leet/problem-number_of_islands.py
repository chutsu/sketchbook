#!/usr/bin/env python3
"""
LeetCode 200: Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and
'0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.
"""


def island_dfs(M, r, c, visited):
  key = f"{r}-{c}"
  if key in visited:
    return
  if r < 0 or r >= len(M):
    return
  if c < 0 or c >= len(M[0]):
    return

  if M[r][c] != 1:
    return

  visited[key] = 1
  island_dfs(M, r + 1, c, visited)
  island_dfs(M, r - 1, c, visited)
  island_dfs(M, r, c + 1, visited)
  island_dfs(M, r, c - 1, visited)


def count_islands(M):
  visited = {}

  num_islands = 0
  for r in range(len(M)):
    for c in range(len(M[0])):
      if f"{r}-{c}" not in visited and M[r][c] != 0:
        island_dfs(M, r, c, visited)
        num_islands += 1

  return num_islands


if __name__ == "__main__":
  # yapf:enable
  M = [
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1]
  ]
  # yapf:disable

  print("Map")
  for row in M:
    print(row)
  print()
  print(count_islands(M))
