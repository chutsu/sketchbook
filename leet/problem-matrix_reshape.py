#!/usr/bin/env python3
"""
LeetCode 566: Reshape the Matrix

In MATLAB, there is a handy function called reshape which can reshape an m x n
matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the
number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original
matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output
the new reshaped matrix; Otherwise, output the original matrix.

"""


def matrix_reshape(mat, r, c):
  m = len(mat)
  n = len(mat[0])

  data = []
  for i in range(m):
    for j in range(n):
      data.append(mat[i][j])

  if len(data) != (r * c):
    return mat

  idx = 0
  out = [[] for _ in range(r)]
  for i in range(r):
    for j in range(c):
      out[i].append(data[idx])
      idx += 1

  return out


if __name__ == "__main__":
  mat = [[1, 2], [3, 4]]
  r = 1
  c = 4
  ans = [[1, 2, 3, 4]]
  out = matrix_reshape(mat, r, c)

  for i in range(r):
    for j in range(c):
      assert (ans[i][j] - out[i][j]) == 0
