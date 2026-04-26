#!/usr/bin/env python3
"""
LeetCode 1089: Duplicate Zeros

Given a fixed-length integer array arr, duplicate each occurrence of zero,
shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do
the above modifications to the input array in place and do not return anything.

--------------------------------------------------------------------------------

Example 1:

Input:

  arr = [1,0,2,3,0,4,5,0]

Output:

  [1,0,0,2,3,0,0,4]

--------------------------------------------------------------------------------

Example 2:

Input:

  arr = [1,2,3]

Output:

  [1,2,3]

"""


def duplicate_zeros(arr):
  num_zeros = arr.count(0)
  N = len(arr)

  for i in range(N - 1, -1, -1):
    if i + num_zeros < N:
      arr[i + num_zeros] = arr[i]

    if arr[i] == 0:
      num_zeros -= 1
      if i + num_zeros < N:
        arr[i + num_zeros] = 0

    if num_zeros == 0:
      break


if __name__ == "__main__":
  arr = [1, 0, 2, 3, 0, 4, 5, 0]
  duplicate_zeros(arr)
  assert arr == [1, 0, 0, 2, 3, 0, 0, 4]
