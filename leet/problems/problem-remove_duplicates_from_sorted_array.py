#!/usr/bin/env python3
"""
LeetCode 26: Remove duplicates from sorted array

Given an integer array nums sorted in non-decreasing order, remove the
duplicates in-place such that each unique element appears only once. The
relative order of the elements should be kept the same. Then return the number
of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you
need to do the following things:

- Change the array nums such that the first k elements of nums contain the
  unique elements in the order they were present in nums initially. The
  remaining elements of nums are not important as well as the size of nums.
- Return k.

"""


def remove_dups(nums):
  visited = set()
  index = 0

  for i, v in enumerate(nums):
    if not v in visited:
      nums[index] = nums[i]
      index += 1
    visited.add(v)

  return index


if __name__ == "__main__":
  nums = [1, 1, 2]
  k = remove_dups(nums)
  assert set(nums[:k]) == set([1, 2])

  nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
  k = remove_dups(nums)
  assert set(nums[:k]) == set([0, 1, 2, 3, 4])
