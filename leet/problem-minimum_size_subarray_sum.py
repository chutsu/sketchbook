#!/usr/bin/env python3
"""
LeetCode 209: Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, return
the minimal length of a subarray whose sum is greater than or equal to target.
If there is no such subarray, return 0 instead.

Example:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem
constraint.
"""


def min_subarray(nums, target):
  result = float("inf")
  left = 0
  total = 0

  for right in range(len(nums)):
    total += nums[right]

    while total >= target:
      result = min(result, right - left + 1)
      total -= nums[left]
      left += 1

  return result if result != float("inf") else 0


target = 7
nums = [2, 3, 1, 2, 4, 3]
assert min_subarray(nums, target) == 2
