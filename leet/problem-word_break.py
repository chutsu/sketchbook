#!/usr/bin/env python3
# LeetCode 139: Word Break [Medium]


def dfs(self, s, word_set, memo):
  if s in memo:
    return memo[s]

  if s in word_set:
    return True

  for i in range(1, len(s)):
    prefix = s[:i]
    if prefix in word_set and dfs(s[i:], word_set, memo):
      memo[s] = True
      return True

  memo[s] = False
  return False


def word_break(s, word_dict):
  memo = {}
  word_set = set(word_dict)
  return dfs(s, word_set, memo)
