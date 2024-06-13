#!/usr/bin/env python3
"""
LeetCode 235: Lowest Common Ancestor of a Binary Search Tree

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of
two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is
defined between two nodes p and q as the lowest node in T that has both p and q
as descendants (where we allow a node to be a descendant of itself).”
"""


class TreeNode:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right


def lowest_common_ancestor(root, p, q):
  if not root or root == p or root == q:
    return root

  left = lowest_common_ancestor(root.left, p, q)
  right = lowest_common_ancestor(root.right, p, q)

  if left and right:
    return root

  return left or right


if __name__ == "__main__":
  # Tree:
  #        A
  #       / \
  #      B   C
  #         / \
  #        D   E
  #       /
  #       F
  F = TreeNode("F")
  D = TreeNode("D", F)
  E = TreeNode("E")
  C = TreeNode("C", D, E)
  B = TreeNode("B")
  A = TreeNode("A", B, C)

  ancestor = lowest_common_ancestor(A, F, E)
  print(ancestor.value)
