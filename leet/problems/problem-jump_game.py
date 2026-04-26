#!/usr/bin/env python3
"""
LeetCode 55: JumpGame

You are given an integer array nums. You are initially positioned at the
array's first index, and each element in the array represents your maximum jump
length at that position.

Return true if you can reach the last index, or false otherwise.


Input: nums = [2, 3, 1, 1, 4]
Output: true
Explanation: You can reach the last index from the first:
  Starting at index 0 with max jump length of 2: 0 -> 2
  Starting at index 2 with max jump length of 1: 2 -> 3
  Starting at index 3 with max jump length of 1: 3 -> 4
"""


def jump_game(nums):
  goal = len(nums) - 1

  for i in range(len(nums) - 1, -1, -1):
    if i + nums[i] >= goal:
      goal = i

  return goal == 0


if __name__ == "__main__":
  nums = [2, 3, 1, 1, 4]
  assert jump_game(nums) is True

  nums = [3, 2, 1, 0, 4]
  assert jump_game(nums) is False
