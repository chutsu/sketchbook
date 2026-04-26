#!/usr/bin/env python3


def valid_palindrome(s):
  string = ""
  for i in s:
    if i.isalnum() is True:
      string += i.lower()

  return string == string[::-1]


if __name__ == "__main__":
  s = "A man, a plan, a canal: Panama"
  assert (valid_palindrome(s) is True)

  s = "race a car"
  assert (valid_palindrome(s) is False)

  s = " "
  assert (valid_palindrome(s) is True)
