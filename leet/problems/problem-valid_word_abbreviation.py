#!/usr/bin/env python3
"""
LeetCode 408: Valid Word Abbreviation
-------------------------------------
A string can be abbreviated by replacing any number of non-adjacent, non-empty
substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

    "s10n" ("s ubstitutio n")
    "sub4u4" ("sub stit u tion")
    "12" ("substitution")
    "su3i1u2on" ("su bst i t u ti on")
    "substitution" (no substrings replaced)

The following are not valid abbreviations:

    "s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
    "s010n" (has leading zeros)
    "s0ubstitution" (replaces an empty substring)

Given a string word and an abbreviation abbr, return whether the string matches
the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.

"""

def valid_word_abbr(word, abbr):
  i = len(word)
  j = len(abbr)
  m = 1
  prev = None

  while i > 0 and j > 0:
    c1 = word[i - 1]
    c2 = abbr[j - 1]

    if c1 == c2:
      i -= 1
      j -= 1
      m = 1
      if prev == 0:
        return False

    elif c2.isnumeric():
      i -= int(c2) * m
      j -= 1
      m *= 10
      prev = int(c2)

    else:
      return False

  return i == j and i == 0


if __name__ == "__main__":
  word = "internationalization"
  abbr = "i12iz4n"
  assert valid_word_abbr(word, abbr) is True

  word = "apple"
  abbr = "a2e"
  assert valid_word_abbr(word, abbr) is False
