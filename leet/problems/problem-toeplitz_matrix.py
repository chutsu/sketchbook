#!/usr/bin/env python3
"""
LeetCode 766: Toeplitz Matrix
-----------------------------
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return
false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the
same elements.
"""

def toeplitz_matrix(A):
  m = len(A)
  n = len(A[0])

  for i in range(1, m):
    for j in range(1, n):
      if A[i - 1][j - 1] != A[i][j]:
        return False

  return True


if __name__ == "__main__":
  # yapf:disable
  A = [
    [1, 2, 3, 4],
    [5, 1, 2, 3],
    [9, 5, 1, 2]
  ]
  # yapf:enable
  assert toeplitz_matrix(A) is True
