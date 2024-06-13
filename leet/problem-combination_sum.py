#!/usr/bin/env python3
"""
LeetCode 39: Combination sum

Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers
sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two
combinations are unique if the frequency of at least one of the chosen numbers
is different.

The test cases are generated such that the number of unique combinations that
sum up to target is less than 150 combinations for the given input.
"""


def dfs(candidates, combinations, current_sum, index, target, results):
  if current_sum == target:
    results.append(combinations)
    return

  if current_sum > target:
    return

  for i in range(index, len(candidates)):
    dfs(candidates, combinations + [candidates[i]], current_sum + candidates[i],
        i, target, results)


def combination_sum(candidates, target):
  results = []
  dfs(candidates, [], 0, 0, target, results)
  return results


candidates = [2, 3, 6, 7]
target = 7
print(combination_sum(candidates, target))

candidates = [2, 3, 5]
target = 8
print(combination_sum(candidates, target))
