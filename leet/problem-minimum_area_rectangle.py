#!/usr/bin/env python3
"""
LeetCode 939: Minimum Area Rectangle

You are given an array of points in the X-Y plane points where points[i] = [xi,
yi].

Return the minimum area of a rectangle formed from these points, with sides
parallel to the X and Y axes. If there is not any such rectangle, return 0.

Example:
Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
"""


def find_minimum_rectangle(points):
  result = float("inf")
  visited = set()

  for x, y in points:
    for xv, yv in visited:
      if (xv, y) in visited and (x, yv) in visited:
        area = abs(xv - x) * abs(yv - y)
        result = min(result, area)
    visited.add((x, y))

  return result if result != float("inf") else 0


if __name__ == "__main__":
  points = [[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]
  output = 4
  assert find_minimum_rectangle(points) == output

  points = [[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]]
  output = 2
  assert find_minimum_rectangle(points) == output
