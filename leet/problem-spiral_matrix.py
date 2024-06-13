#!/usr/bin/env python3
"""
LeetCode 54: Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.

Input:
[[1,2,3],
 [4,5,6],
 [7,8,9]]

Output:
 [1,2,3,6,9,8,7,4,5]

Input:
[[1,2,3,4],
 [5,6,7,8],
 [9,10,11,12]]

Output:
 [1,2,3,4,8,12,11,10,9,5,6,7]

"""

def spiral_order(matrix):
  if not matrix:
    return []

  num_rows = len(matrix)
  num_cols = len(matrix[0])

  top = 0
  bottom = num_rows - 1
  left = 0
  right = num_cols - 1

  result = []
  while len(result) < (num_rows * num_cols):
    # Left -> Right
    for i in range(left, right + 1):
      result.append(matrix[top][i])
    top += 1
    if len(result) == (num_rows * num_cols):
      break

    # Top-right -> Bottom right
    for i in range(top, bottom + 1):
      result.append(matrix[i][right])
    right -= 1
    if len(result) == (num_rows * num_cols):
      break

    # Bottom right  -> Bottom left
    for i in range(right, left - 1, -1):
      result.append(matrix[bottom][i])
    bottom -= 1
    if len(result) == (num_rows * num_cols):
      break

    # Bottom left -> Top Left
    for i in range(bottom, top - 1, -1):
      result.append(matrix[i][left])
    left += 1
    if len(result) == (num_rows * num_cols):
      break

  return result


def spiral_order_compact(matrix):
  result = []
  while matrix:
    result.append(matrix.pop(0))
    matrix = list(zip(*matrix))[::-1]
  return result


if __name__ == "__main__":
  matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  solution = [1, 2, 3, 6, 9, 8, 7, 4, 5]

  result = spiral_order(matrix)
  assert (solution[i] == result[i] for i in range(len(solution)))

  result = spiral_order_compact(matrix)
  assert (solution[i] == result[i] for i in range(len(solution)))
