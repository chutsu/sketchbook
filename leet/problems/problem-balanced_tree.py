#!/usr/bin/env python3
"""
LeetCode 110: Balance Binary Tree

Given a binary tree, determine if it is height-balanced.

A height-balanced binary tree is a binary tree in which the depth of the two
subtrees of every node never differs by more than one.
"""

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def is_balanced(n: TreeNode | None):
  if not n:
    return True

  def max_depth(node):
    if node is None:
      return 0
    return 1 + max(max_depth(node.left), max_depth(node.right))

  left = max_depth(n.left)
  right = max_depth(n.right)
  return abs(left - right) <= 1 and is_balanced(n.left) and is_balanced(n.right)



if __name__ == "__main__":
  """
      3
    9   20
      15   7
  """
  n15 = TreeNode(15)
  n7 = TreeNode(7)
  n9 = TreeNode(9)
  n20 = TreeNode(20, n15, n7)
  n3 = TreeNode(3, n9, n20)
  assert is_balanced(n3)
