#!/usr/bin/env python3
"""
LeetCode 188: Rotate Array

Given an integer array nums, rotate the array to the right by k steps, where k
is non-negative.

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""


def rev(nums, l, r):
  while r >= l:
    tmp = nums[l]
    nums[l] = nums[r]
    nums[r] = tmp
    l += 1
    r -= 1


def rotate_array(nums, k):
  n = len(nums)
  rev(nums, 0, n - 1)  # Reverse entire array
  rev(nums, 0, k - 1)  # Reverse front portion
  rev(nums, k, n - 1)  # Reverse end portion


if __name__ == "__main__":
  nums = [1, 2, 3, 4, 5, 6, 7]
  k = 3

  rotate_array(nums, k)
  assert nums == [5, 6, 7, 1, 2, 3, 4]
