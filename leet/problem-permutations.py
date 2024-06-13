#!/usr/bin/env python3


def backtrack(nums, visited, results, path):
  if len(path) == len(nums):
    results.append(path)
    return

  for i in nums:
    if i in visited:
      continue

    visited.add(i)
    backtrack(nums, visited, results, path + [i])
    visited.remove(i)


def permute(nums):
  visited = set()
  results = []
  backtrack(nums, visited, results, [])
  return results


if __name__ == "__main__":
  nums = [1, 2, 3]
  print(permute(nums))
