#!/usr/bin/env python3
"""
LeetCode 680: Valid Palindrome II
---------------------------------

Given a string s, return true if the s can be palindrome after deleting at most
one character from it.
"""

def check(s, left, right, deleted=False):
  while left <= right:
    if s[left] != s[right]:
      if deleted:
        return False
      else:
        return check(s, left+1, right, True) or check(s, left, right-1, True)

    left += 1
    right -= 1

  return True


if __name__ == "__main__":
  s = "aba"
  assert check(s, 0, len(s) - 1, False) is True

  s = "abca"
  assert check(s, 0, len(s) - 1, False) is True

  s = "abc"
  assert check(s, 0, len(s) - 1, False) is False
