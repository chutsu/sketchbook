#!/usr/bin/env python3
"""
LeetCode 100: Same Tree

Given the roots of two binary trees p and q, write a function to check if they
are the same or not.

Two binary trees are considered the same if they are structurally identical,
and the nodes have the same value.
"""

class TreeNode:
  def __init__(self, value, left=None, right=None):
    self.left = left
    self.right = right
    self.value = value

  def __str__(self):
    return self.value

  def __repr__(self):
    return str(self.value)


def is_same(p, q):
  def check(a, b):
    if not a and not b:
      return True

    if (not a and b) or (a and not b):
      return False

    if a.value != b.value:
      return False

    return check(a.left, b.left) and check(a.right, b.right)

  return check(p, q)
