#!/usr/bin/env python3
"""
LeetCode 227: Basic Calculator II

Given a string s which represents an expression, evaluate this expression and
return its value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate
results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings
as mathematical expressions, such as eval().
"""


def calculate(s):
  num = 0
  preop = "+"
  stack = []

  for c in s + "+":
    if c.isdigit():
      num = num * 10 + int(c)

    elif c in "+-*/":
      if preop == "+":
        stack.append(num)
      if preop == "-":
        stack.append(-num)
      if preop == "*":
        stack.append(stack.pop() * num)
      if preop == "/":
        stack.append(int(stack.pop() / num))

      preop = c
      num = 0

  return sum(stack)


if __name__ == "__main__":
  s = "3+2*2"
  assert calculate(s) == 7

  s = " 3/2 "
  assert calculate(s) == 1

  s = " 3+5 / 2 "
  assert calculate(s) == 5
