#!/usr/bin/env python3
import heapq

# def seq_digits(low, high):
#   s = "123456789"

#   ans = []
#   for i in range(len(s)):
#     for j in range(i + 1, len(s)):
#       num = int(s[i:j + 1])
#       if num > low and num < high:
#         ans.append(num)
#       elif num > high:
#         break

#   return ans

# low = 1000
# high = 13000
# print(seq_digits(low, high))

# def word_square(words):
#   for i in range(len(words)):
#     for j in range(len(words[i])):
#       try:
#         if words[i][j] != words[j][i]:
#           return False
#       except:
#         return False

#   return True

# words = ["abcd", "bnrt", "crmy", "dtye"]
# print(word_square(words))

# words = ["ball", "area", "read", "lady"]
# print(word_square(words))

# def permutations(nums):
#   def backtrack(nums, path, seen, res):
#     if len(path) == len(nums):
#       res.append(path)
#       return

#     for num in nums:
#       if num in seen:
#         continue

#       seen.add(num)
#       backtrack(nums, path + [num], seen, res)
#       seen.remove(num)

#   path = []
#   seen = set()
#   res = []
#   backtrack(nums, path, seen, res)
#   return res

# nums = [1, 2, 3]
# print(permutations(nums))

# def longest_substring(s):
#   left = 0
#   seen = {}
#   ans = 0

#   for right, c in enumerate(s):
#     if c in seen:
#       left = max(left, seen[c] + 1)

#     ans = max(ans, right - left + 1)
#     seen[c] = right

#   return ans

# s = "abcabcbb"
# print(longest_substring(s))

# s = "pwwkew"
# print(longest_substring(s))

# def merge_intervals(intervals):
#   ans = [intervals[0]]
#   for i, (start, end) in enumerate(intervals[1:]):
#     if ans[-1][1] > start:
#       ans[-1][1] = max(ans[-1][1], end)
#     else:
#       ans.append([start, end])

#   return ans

# intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# # Output: [[1, 6], [8, 10], [15, 18]]
# print(merge_intervals(intervals))

# def flatten(arr):
#   ans = []
#   for x in arr:
#     if type(x) is int:
#       ans.append(x)
#     elif type(x) is list:
#       ans.extend(flatten(x))
#   return ans

# print(flatten([[1, 1], 2, [1, 1]]))

# def perfect_squares(num):
#   dp = [num] * (num + 1)
#   dp[0] = 0

#   for target in range(1, num + 1):
#     j = 1
#     while (j * j) <= target:
#       dp[target] = min(dp[target], dp[target - (j * j)] + 1)
#       j += 1

#   return dp[num]

# print(perfect_squares(10))

# def longest_subsequence(nums, k):
#   n = len(nums)
#   dp = [1] * n

#   for i in range(1, n):
#     for j in range(i):
#       if nums[j] < nums[i] and (nums[i] - nums[j]) <= k:
#         dp[i] = max(dp[i], dp[j] + 1)

#   return max(dp)

# nums = [4, 2, 1, 4, 3, 4, 5, 8, 15]
# k = 3
# print(longest_subsequence(nums, k))


# def min_deviations(nums):
#   mp = {}
#   n = len(nums)
#   min_heap = []
#   heap_max = 0

#   for i, num in enumerate(nums):
#     num_orig = num
#     while num % 2 == 0:
#       num = num // 2
#     min_heap.append((num, max(num_orig, 2 * num)))
#     heap_max = max(heap_max, num)

#   res = float("inf")
#   heapq.heapify(min_heap)
#   while len(min_heap) == len(nums):
#     n, n_max = heapq.heappop(min_heap)
#     res = min(res, heap_max - n)

#     if n < n_max:
#       heapq.heappush(min_heap, (n * 2, n_max))
#       heap_max = max(heap_max, n * 2)

#   return res

# nums = [1, 2, 3, 4]
# print(min_deviations(nums))

# nums = [4, 1, 5, 20, 3]
# print(min_deviations(nums))
