#!/usr/bin/env python3
"""
LeetCode 27: Remove element

Given an integer array nums and an integer val, remove all occurrences of val
in nums in-place. The order of the elements may be changed. Then return the
number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get
accepted, you need to do the following things:

- Change the array nums such that the first k elements of nums contain the
  elements which are not equal to val. The remaining elements of nums are not
  important as well as the size of nums.
- Return k.
"""


def remove_element(nums, val):
  index = 0
  for i, v in enumerate(nums):
    if v != val:
      nums[index] = nums[i]
      index += 1
  return index


if __name__ == "__main__":
  nums = [3, 2, 2, 3]
  val = 3
  assert remove_element(nums, val) == 2
  print(nums[:2])

  nums = [0, 1, 2, 2, 3, 0, 4, 2]
  val = 2
  assert remove_element(nums, val) == 5
  print(nums[:5])
