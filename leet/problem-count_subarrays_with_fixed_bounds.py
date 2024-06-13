#!/usr/bin/env python3
"""
LeetCode 2444: Count Subarrays With Fixed Bounds

You are given an integer array nums and two integers minK and maxK.

A fixed-bound subarray of nums is a subarray that satisfies the following
conditions:

    The minimum value in the subarray is equal to minK.
    The maximum value in the subarray is equal to maxK.

Return the number of fixed-bound subarrays.

A subarray is a contiguous part of an array.

-------------------------------------------------------------------------------

Example 1:

  Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5

Output: 2

  Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].

-------------------------------------------------------------------------------

Example 2:

  Input: nums = [1,1,1,1], minK = 1, maxK = 1

Output: 10

  Explanation: Every subarray of nums is a fixed-bound subarray. There are 10
  possible subarrays.

"""


def count(nums, min_k, max_k):
  ans = 0
  bad = -1
  left = -1
  right = -1

  for i, num in enumerate(nums):
    if num < min_k or num > max_k:
      bad = i

    if num == min_k:
      left = i

    if num == max_k:
      right = i

    ans += max(0, min(left, right) - bad)

  return ans


if __name__ == "__main__":
  nums = [1, 3, 5, 2, 7, 5]
  min_k = 1
  max_k = 5
  assert count(nums, min_k, max_k) == 2

  nums = [1, 1, 1, 1]
  min_k = 1
  max_k = 1
  assert count(nums, min_k, max_k) == 10
