#!/usr/bin/env python3
"""
LeetCode 17: Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given
below. Note that 1 does not map to any letters.
"""


def backtrack(digits, i, curr_str, results):
  mapping = {
      "2": "abc",
      "3": "def",
      "4": "ghi",
      "5": "jkl",
      "6": "mno",
      "7": "pqrs",
      "8": "tuv",
      "9": "wxyz"
  }

  if len(curr_str) == len(digits):
    results.append(curr_str)
    return

  for c in mapping[digits[i]]:
    backtrack(digits, i + 1, curr_str + c, results)


def letter_combinations(digits):
  results = []
  backtrack(digits, 0, "", results)
  if len(digits) == 0:
    return []

  return results


if __name__ == "__main__":
  digits = "23"
  expected_result = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
  result = letter_combinations(digits)
  assert (result == expected_result)
