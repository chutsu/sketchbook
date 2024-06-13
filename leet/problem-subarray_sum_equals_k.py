#!/usr/bin/env python3
"""
LeetCode 560: Subarray sum equals k
-----------------------------------
Given an array of integers nums and an integer k, return the total number of
subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
"""
from collections import defaultdict

def subarray_equals(nums, k):
  count = 0
  cumsum = 0
  d = defaultdict(int)
  d[0] = 1

  for n in nums:
    # Accumulative sum
    cumsum += n

    if (cumsum - k) in d:
      count += d[(cumsum - k)]

    # Track cumulative sum
    d[cumsum] += 1

  import pprint
  pprint.pprint(d)

  return count


if __name__ == "__main__":
  # nums = [1, 1, 1]
  # k = 2
  # assert subarray_equals(nums, k) == 2

  nums = [1, 2, 3]
  k = 4
  print(subarray_equals(nums, k))
  # assert subarray_equals(nums, k) == 2
