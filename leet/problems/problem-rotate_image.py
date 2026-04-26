#!/usr/bin/env python3
"""
LeetCode 48: Rotate Image
-------------------------
You are given an n x n 2D matrix representing an image, rotate the image by 90
degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input
2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""
import numpy as np


def rotate_image(matrix):
  m = len(matrix)
  n = len(matrix[0])

  # Transpose
  for i in range(m):
    for j in range(i):
      tmp = matrix[i][j]
      matrix[i][j] = matrix[j][i]
      matrix[j][i] = tmp

  # Reverse each row
  for i in range(m):
    left = 0
    right = n - 1
    while left < right:
      tmp = matrix[i][left]
      matrix[i][left] = matrix[i][right]
      matrix[i][right] = tmp
      left += 1
      right -= 1


def rotate_image_inplace(matrix):
  m = len(matrix)
  n = len(matrix[0])

  top = 0
  bottom = n - 1
  while top < bottom:
    left = top
    right = bottom

    for i in range(right - left):
      top_left = matrix[top][left + i]

      matrix[top][left + i] = matrix[bottom - i][left]
      matrix[bottom - i][left] = matrix[bottom][right - i]
      matrix[bottom][right - i] = matrix[top + i][right]
      matrix[top + i][right] = top_left

    top += 1
    bottom -= 1


def print_matrix(A):
  m = len(A)
  n = len(A[0])

  for i in range(m):
    for j in range(n):
      print(A[i][j], end=" ")
    print()


if __name__ == "__main__":
  # yapf:disable
  A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
  ]
  # yapf:enable

  # yapf:disable
  B = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
  ]
  # yapf:enable

  # rotate_image(A)
  # rotate_image_inplace(A)
  # print_matrix(A)

  rotate_image_inplace(B)
  print_matrix(B)
