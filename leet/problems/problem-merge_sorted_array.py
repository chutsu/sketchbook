#!/usr/bin/env python3
"""
LeetCode 88: Merge sorted array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing
order, and two integers m and n, representing the number of elements in nums1
and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be
stored inside the array nums1. To accommodate this, nums1 has a length of m +
n, where the first m elements denote the elements that should be merged, and
the last n elements are set to 0 and should be ignored. nums2 has a length of
n.

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
"""


def merge(nums1, m, nums2, n):
  a = m - 1
  b = n - 1
  i = m + n - 1

  while i >= 0:
    if a >= 0 and b >= 0 and nums1[a] > nums2[b]:
      nums1[i] = nums1[a]
      a -= 1
    elif a >= 0 and b >= 0 and nums1[a] <= nums2[b]:
      nums1[i] = nums2[b]
      b -= 1

    i -= 1


if __name__ == "__main__":
  nums1 = [1, 2, 3, 0, 0, 0]
  m = 3
  nums2 = [2, 5, 6]
  n = 3

  print(nums1)
  print(nums2)
  merge(nums1, m, nums2, n)
  print(nums1)
