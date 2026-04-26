#!/usr/bin/env python3
"""
LeetCode 1291: Sequential Digits

An integer has sequential digits if and only if each digit in the number is one
more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive
that have sequential digits.


-------------------------------------------------------------------------------

Example 1:

  Input: low = 100, high = 300

Output: [123,234]

-------------------------------------------------------------------------------

Example 2:

  Input: low = 1000, high = 13000

Output: [1234,2345,3456,4567,5678,6789,12345]

"""

def process(low, high):
  s = "123456789"

  ans = []
  for left in range(len(s)):
    for right in range(left, len(s)):
      num = int(s[left:right+1])
      if num >= low and num <= high:
        ans.append(num)
      elif num > high:
        break

  return ans


if __name__ == "__main__":
  low = 100
  high = 300
  print(process(low, high))

  low = 1000
  high = 13000
  print(process(low, high))
