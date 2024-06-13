#!/usr/bin/env python3
"""
LeetCode 1143: Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common
subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string
with some characters (can be none) deleted without changing the relative order
of the remaining characters.

    For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both
strings.


-----------------------------------------------------------------------------

Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

-----------------------------------------------------------------------------

Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

-----------------------------------------------------------------------------

Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

"""


def longest_subsequence(s1, s2):
  def fn(s1, s2, i, j, cache):
    if (i, j) in cache:
      return cache[(i, j)]

    if i == len(s1) or j == len(s2):
      cache[(i, j)] = 0

    elif s1[i] == s2[j]:
      cache[(i, j)] = 1 + fn(s1, s2, i + 1, j + 1, cache)

    else:
      cache[(i, j)] = max(fn(s1, s2, i + 1, j, cache),
                          fn(s1, s2, i, j + 1, cache))

    return cache[(i, j)]

  cache = {}
  return fn(s1, s2, 0, 0, cache)


def longest_subsequence2(s1, s2):
  m = len(s1)
  n = len(s2)
  cache = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

  for i in range(1, m + 1):
    for j in range(1, n + 1):
      if s1[i - 1] == s2[j - 1]:
        cache[i][j] = 1 + cache[i - 1][j - 1]
      else:
        cache[i][j] = max(cache[i - 1][j], cache[i][j - 1])

  return cache[m][n]


if __name__ == "__main__":
  text1 = "abcde"
  text2 = "ace"
  assert longest_subsequence(text1, text2) == 3
  assert longest_subsequence2(text1, text2) == 3
