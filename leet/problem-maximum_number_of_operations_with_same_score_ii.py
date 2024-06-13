#!/usr/bin/env python3
"""
LeetCode 3040: Maximum number of operations with same score II

Given an array of integers called nums, you can perform any of the following
operation while nums contains at least 2 elements:

    Choose the first two elements of nums and delete them.
    Choose the last two elements of nums and delete them.
    Choose the first and the last elements of nums and delete them.

The score of the operation is the sum of the deleted elements.

Your task is to find the maximum number of operations that can be performed,
such that all operations have the same score.

Return the maximum number of operations possible that satisfy the condition
mentioned above.

-------------------------------------------------------------------------------

Example 1:

Input:

  nums = [3,2,1,2,3,4]

Output:

  3

Explanation: We perform the following operations:
- Delete the first two elements, with score 3 + 2 = 5, nums = [1,2,3,4].
- Delete the first and the last elements, with score 1 + 4 = 5, nums = [2,3].
- Delete the first and the last elements, with score 2 + 3 = 5, nums = [].

We are unable to perform any more operations as nums is empty.

-------------------------------------------------------------------------------

Example 2:

Input:

  nums = [3,2,6,1,4]

Output:

  2

Explanation: We perform the following operations:
- Delete the first two elements, with score 3 + 2 = 5, nums = [6,1,4].
- Delete the last two elements, with score 1 + 4 = 5, nums = [6].
It can be proven that we can perform at most 2 operations.

"""


def max_ops(nums):
  def dfs(s, c, l, r):
    if r <= l:
      return 0

    if (l, r) not in c:
      max_ops1 = 1 + dfs(s, c, l + 2, r) if sum(nums[l:l + 2]) == s else 0
      max_ops2 = 1 + dfs(s, c, l, r - 2) if sum(nums[r - 1:r + 1]) == s else 0
      max_ops3 = 1 + dfs(s, c, l + 1, r - 1) if nums[l] + nums[r] == s else 0
      c[(l, r)] = max(max_ops1, max_ops2, max_ops3)

    return c[(l, r)]

  max_ops1 = dfs(sum(nums[:2]), {}, 0, len(nums) - 1)
  max_ops2 = dfs(sum(nums[-2:]), {}, 0, len(nums) - 1)
  max_ops3 = dfs(nums[0] + nums[-1], {}, 0, len(nums) - 1)
  return max(max_ops1, max_ops2, max_ops3)


if __name__ == "__main__":
  nums = [3, 2, 1, 2, 3, 4]
  print(max_ops(nums))

  nums = [3, 2, 6, 1, 4]
  print(max_ops(nums))
