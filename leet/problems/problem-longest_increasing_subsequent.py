#!/usr/bin/env python3
"""
LeetCode 300: Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly
increasing subsequence.
"""

def longest_subsequence(nums):
  n = len(nums)
  dp = [1] * n

  for i in range(1, n):
    for j in range(i):
      if nums[j] < nums[i]:
        dp[i] = max(dp[i], dp[j] + 1)

  return max(dp)


if __name__ == "__main__":
  nums = [10, 9, 2, 5, 3, 7, 101, 18]
  assert longest_subsequence(nums) == 4
