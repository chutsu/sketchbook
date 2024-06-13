#!/usr/bin/env python3


def three_sum(nums, target):
  nums = sorted(nums)
  triplets = []

  for i in range(len(nums)):
    # Skip duplicates
    if i > 0 and nums[i - 1] == nums[i]:
      continue

    left = i + 1
    right = len(nums) - 1

    while left < right:
      current_sum = nums[i] + nums[left] + nums[right]

      # Target sum reached
      if current_sum == target:
        # Add to triplets
        triplets.append([nums[i], nums[left], nums[right]])
        left += 1
        right -= 1

        # Skip duplicates on the left pointer
        while left < right and nums[left - 1] == nums[left]:
          left += 1

        # Skip duplicates on the left pointer
        while left < right and nums[right + 1] == nums[right]:
          right -= 1

      elif current_sum < 0:
        left += 1

      else:
        right -= 1

  return triplets


if __name__ == "__main__":
  nums = [-1, 0, 1, 2, -1, -4]
  target = 0
  print(three_sum(nums, target))
