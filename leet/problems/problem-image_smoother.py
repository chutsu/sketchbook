#!/usr/bin/env python3
"""
LeetCode 661. Image Smoother

An image smoother is a filter of the size 3 x 3 that can be applied to each
cell of an image by rounding down the average of the cell and the eight
surrounding cells (i.e., the average of the nine cells in the blue smoother).
If one or more of the surrounding cells of a cell is not present, we do not
consider it in the average (i.e., the average of the four cells in the red
smoother).
"""
import numpy as np


def image_smoother(img):
  m = len(img)
  n = len(img[0])

  out = np.zeros((m, n))
  for r in range(m):
    for c in range(n):

      total = 0
      N = 0
      for i in range(r - 1, r + 2):
        for j in range(c - 1, c + 2):
          if i < 0 or i >= m or j < 0 or j >= n:
            continue
          total += img[i][j]
          N += 1
      out[r][c] = np.floor(total / N)

  return out


if __name__ == "__main__":
  img = np.array([[100, 200, 100], [200, 50, 200], [100, 200, 100]])
  ans = np.array([[137, 141, 137], [141, 138, 141], [137, 141, 137]])
  out = image_smoother(img)
  assert np.array_equal(out, ans)
