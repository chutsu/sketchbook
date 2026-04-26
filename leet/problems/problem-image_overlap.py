#!/usr/bin/env python3
"""
LeetCode 835: Image Overlap

You are given two images, img1 and img2, represented as binary, square matrices
of size n x n. A binary matrix has only 0s and 1s as values.

We translate one image however we choose by sliding all the 1 bits left, right,
up, and/or down any number of units. We then place it on top of the other
image. We can then calculate the overlap by counting the number of positions
that have a 1 in both images.

Note also that a translation does not include any kind of rotation. Any 1 bits
that are translated outside of the matrix borders are erased.

Return the largest possible overlap.
"""
import collections


def image_overlap(A, B):
  # Get coordinates of non-zero values
  A_points = []
  B_points = []
  for i in range(len(A)):
    for j in range(len(A[0])):
      if A[i][j]:
        A_points.append((i, j))
      if B[i][j]:
        B_points.append((i, j))

  # Loop through pairs and find the most overlap transformation
  d = collections.defaultdict(int)
  for ai, aj in A_points:
    for bi, bj in B_points:
      d[(bi - ai, bj - aj)] += 1

  # Get max overlaps
  max_overlaps = 0
  for k, v in d.items():
    max_overlaps = max(max_overlaps, v)

  return max_overlaps


if __name__ == "__main__":
  A = [[1, 1, 0], [0, 1, 0], [0, 1, 0]]
  B = [[0, 0, 0], [0, 1, 1], [0, 0, 1]]
  assert (image_overlap(A, B) == 3)
