#!/usr/bin/env python3
"""
LeetCode 283: Move Zeros

Given an integer array nums, move all 0's to the end of it while maintaining
the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""


def move_zeros(nums):
  slow = 0

  for fast in range(0, len(nums)):
    if nums[fast] != 0:
      tmp = nums[fast]
      nums[fast] = nums[slow]
      nums[slow] = tmp
      slow += 1


if __name__ == "__main__":
  nums = [0, 1, 0, 3, 12]
  move_zeros(nums)
  print(nums)
