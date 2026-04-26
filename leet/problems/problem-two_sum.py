#!/usr/bin/env python3


def two_sum_with_map(nums, target):
  # Create a map with value-index pair
  m = {}
  for i, n in enumerate(nums):
    m[n] = i

  for i, n in enumerate(nums):
    key = target - n
    if key in m and m[key] != i:
      return [i, m[key]]


def two_sum_with_two_pointers(nums, target):
  nums = sorted(nums)
  left = 0
  right = len(nums) - 1

  while left < right:
    s = nums[left] + nums[right]
    if s == target:
      return [left, right]

    if s > target:
      right -= 1
    else:
      left += 1

  return []


if __name__ == "__main__":
  nums = [2, 7, 11, 15]
  target = 9
  result = two_sum_with_map(nums, target)
  assert (result[0] == 0 and result[1] == 1)

  nums = [3, 2, 4]
  target = 6
  result = two_sum_with_map(nums, target)
  assert (result[0] == 1 and result[1] == 2)

  nums = [3, 3]
  target = 6
  result = two_sum_with_map(nums, target)
  assert (result[0] == 0 and result[1] == 1)

  nums = [2, 7, 11, 15]
  target = 13
  result = two_sum_with_two_pointers(nums, target)
  assert (result[0] == 0 and result[1] == 2)
