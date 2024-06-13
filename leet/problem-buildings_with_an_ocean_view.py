#!/usr/bin/env python3
"""
LeetCode 1762: Buildings with an Ocean View

There are n buildings in a line. You are given an integer array heights of size
n that represents the heights of the buildings in the line.

The ocean is to the right of the buildings. A building has an ocean view if the
building can see the ocean without obstructions. Formally, a building has an
ocean view if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view,
sorted in increasing order.
"""


def find(heights):
  results = [len(heights) - 1]

  for i in range(len(heights) - 2, -1, -1):
    if heights[i] > heights[results[-1]]:
      results.append(i)

  results.reverse()
  return results


if __name__ == "__main__":
  heights = [4, 2, 3, 1]

  print(find(heights))
