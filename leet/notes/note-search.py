#!/usr/bin/env python3


def binary_search(nums, target):
  left = 0
  right = len(nums) - 1

  while left <= right:
    mid = left + int((right - left) / 2)

    if nums[mid] == target:
      return mid

    elif nums[mid] > target:
      right = mid - 1

    else:
      left = mid + 1

  return -1


def binary_search_rotated_list(nums, target):
  left = 0
  right = len(nums) - 1

  while left <= right:
    mid = left + int((right - left) / 2)

    if nums[mid] == target:
      return mid

    if nums[mid] < nums[right]:
      if nums[mid] < target and target <= nums[right]:
        left = mid + 1
      else:
        right = mid - 1

    else:
      if nums[left] <= target and target < nums[mid]:
        right = mid - 1
      else:
        left = mid + 1

  return -1


if __name__ == "__main__":
  # Standard binary search
  nums = [1, 2, 3, 4, 5, 6, 7]
  index = binary_search(nums, 6)
  assert (index == 5)
  index = binary_search(nums, 2)
  assert (index == 1)

  # Perform binary search on a potentially pivoted sorted list
  nums = [4, 5, 6, 7, 0, 1, 2]
  target = 0
  index = binary_search_rotated_list(nums, target)
  assert (index == 4)
