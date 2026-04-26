#!/usr/bin/env python3
"""
LeetCode 11: Container With Most Water

You are given an integer array height of length n. There are n vertical lines
drawn such that the two endpoints of the ith line are (i, 0) and (i,
height[i]).

Find two lines that together with the x-axis form a container, such that the
container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""


def max_area_container(heights):
  max_area = 0

  # O(n^2) solution
  # for l in range(len(heights)):
  #     for r in range(len(heights)):
  #         area = (r - l) * min(heights[l], heights[r])
  #         max_area = max(max_area, area)

  l = 0
  r = len(heights) - 1
  while l < r:
    area = (r - l) * min(heights[l], heights[r])
    max_area = max(max_area, area)

    if heights[l] < heights[r]:
      l += 1
    else:
      r -= 1

  return max_area


if __name__ == "__main__":
  heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
  expected_result = 49
  result = max_area_container(heights)
  assert (expected_result == result)
