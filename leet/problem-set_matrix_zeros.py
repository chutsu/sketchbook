#!/usr/bin/env python3
"""
LeetCode 73: Set matrix zeros

Given an m x n integer matrix matrix, if an element is 0, set its entire row
and column to 0's. You must do it in place.

Examples:

Input:
matrix = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]

Output:
[[1,0,1],
 [0,0,0],
 [1,0,1]]
"""


def matrix_zeros(A):
  m = len(A)
  n = len(A[0])

  zero_rows = [False] * m
  zero_cols = [False] * n
  for i in range(m):
    for j in range(n):
      if A[i][j] == 0:
        zero_rows[i] = True
        zero_cols[j] = True

  for i in range(m):
    for j in range(n):
      if zero_rows[i] or zero_cols[j]:
        A[i][j] = 0

  return A


if __name__ == "__main__":
  A = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
  expected = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
  assert matrix_zeros(A) == expected

  A = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
  expected = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
  assert matrix_zeros(A) == expected
