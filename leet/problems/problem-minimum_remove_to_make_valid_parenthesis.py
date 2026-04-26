#!/usr/bin/env python3
"""
LeetCode 1249: Minimum Remove to Make Valid Parenthesis

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any
positions ) so that the resulting parentheses string is valid and return any
valid string.

Formally, a parentheses string is valid if and only if:

- It is the empty string, contains only lowercase characters, or
- It can be written as AB (A concatenated with B), where A and B are valid
  strings, or
- It can be written as (A), where A is a valid string.
"""

def minimum_remove(s):
  s = list(s)
  stack = []

  for i, c in enumerate(s):
    if c == "(":
      stack.append(i)

    elif c == ")":
      if len(stack):
        stack.pop(-1)
      else:
        s[i] = ""

  while len(stack):
    s[stack.pop(-1)] = ""

  return "".join(s)


if __name__ == "__main__":
  s = "lee(t(c)o)de)"
  assert minimum_remove(s) == "lee(t(c)o)de"

  s = "a)b(c)d"
  assert minimum_remove(s) == "ab(c)d"

  s = "))(("
  assert minimum_remove(s) == ""
