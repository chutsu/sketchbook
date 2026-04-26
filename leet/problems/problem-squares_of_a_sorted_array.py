#!/usr/bin/env python3
"""
LeetCode 977: Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, return an array of
the squares of each number sorted in non-decreasing order.

--------------------------------------------------------------------------------

Example 1:

Input:

  nums = [-4,-1,0,3,10]

Output:

  [0,1,9,16,100]

Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

--------------------------------------------------------------------------------

Example 2:

Input:

  nums = [-7,-3,2,3,11]

Output:

  [4,9,9,49,121]

"""


def sort_squares(nums):
  # Main intuition is to:
  # - iterate positive numbers in order
  # - iterate negative numbers in reverse order
  N = len(nums)
  result = [0] * N
  left = 0
  right = N - 1

  for i in range(N - 1, -1, -1):
    if abs(nums[left]) < abs(nums[right]):
      result[i] = nums[right] * nums[right]
      right -= 1
    else:
      result[i] = nums[left] * nums[left]
      left += 1

  return result


if __name__ == "__main__":
  nums = [-7, -3, 2, 3, 11]
  result = sort_squares(nums)
  assert result == [4, 9, 9, 49, 121]
