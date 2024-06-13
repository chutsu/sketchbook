#!/usr/bin/env python3
"""
LeetCode 543: Diameter of binary tree

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two
nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges
between them.
"""
import numpy as np


class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def dfs(n, d):
  left, d_left = dfs(n.left, d) if n.left else (0, d)
  right, d_right = dfs(n.right, d) if n.right else (0, d)
  d = np.max([d, left + right, d_left, d_right])
  return 1 + max(left, right), d


def binary_tree_diameter(root):
  return dfs(root, 0)[1]


if __name__ == "__main__":
  """
  Tree:

      1
    2   3
  4   5

  """
  node5 = TreeNode(5)
  node4 = TreeNode(4)
  node3 = TreeNode(3)
  node2 = TreeNode(2, node4, node5)
  node1 = TreeNode(1, node2, node3)
  assert binary_tree_diameter(node1) == 3
  """
  Tree:

      1
     2 3
      4 5
     6   7
    8     9

  """
  node9 = TreeNode(9)
  node8 = TreeNode(8)
  node7 = TreeNode(7, None, node9)
  node6 = TreeNode(6, node8)
  node5 = TreeNode(5, None, node7)
  node4 = TreeNode(4, node6)
  node3 = TreeNode(3, node4, node5)
  node2 = TreeNode(2)
  node1 = TreeNode(1, node2, node3)
  assert binary_tree_diameter(node1) == 6
