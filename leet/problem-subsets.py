#!/usr/bin/env python3
# LeetCode 78: Subsets [Medium]


def dfs(nums, path, index, results):
  if len(path) > len(nums):
    return

  results.append(path)

  for i in range(index, len(nums)):
    dfs(nums, path + [nums[i]], i + 1, results)


def subsets(nums):
  path = []
  index = 0
  results = []
  dfs(nums, path, index, results)
  return results


if __name__ == "__main__":
  nums = [1, 2, 3]
  solution = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
  results = subsets(nums)
  print(solution)
  print(results)
