#!/usr/bin/env python3
"""
LeetCode 50. Pow(x, n)
----------------------
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
"""

def myPow(x, n):
  if n == 0:
    return 1
  elif n == 1:
    return x
  elif n == -1:
    return 1.0 / x

  return myPow(x, n // 2) * myPow(x, n // 2) * myPow(x, n % 2)

if __name__ == "__main__":
  assert myPow(2, 10) == 1024
