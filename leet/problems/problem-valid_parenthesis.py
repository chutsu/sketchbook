#!/usr/bin/env python3


def valid_parenthesis(s):
  symbols = {"(": ")", "[": "]", "{": "}"}

  stack = []
  for x in s:
    if len(stack) and symbols[stack[-1]] == x:
      stack.pop()
    else:
      stack.append(x)

  return len(stack) == 0


if __name__ == "__main__":
  s = "()"
  assert (valid_parenthesis(s) is True)

  s = "()[]{}"
  assert (valid_parenthesis(s) is True)

  s = "(]"
  assert (valid_parenthesis(s) is False)
