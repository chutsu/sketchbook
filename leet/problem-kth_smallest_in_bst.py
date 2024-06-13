#!/usr/bin/env python3
"""
LeetCode 230: Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k, return the kth
smallest value (1-indexed) of all the values of the nodes in the tree.
"""


class TreeNode:
  def __init__(self, value=None, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right


def _inorder_dfs(root, k, path):
  if root is None:
    return

  # Traverse left subtree
  _inorder_dfs(root.left, k, path)

  # Add to path
  if len(path) == k:
    return
  path.append(root.value)

  # Traverse right subtree
  _inorder_dfs(root.right, k, path)


def kth_smallest(root, k):
  path = []
  _inorder_dfs(root, k, path)
  return path[-1]


if __name__ == "__main__":
  # Test case 1
  node_2 = TreeNode(2)
  node_1 = TreeNode(1, None, node_2)
  node_4 = TreeNode(4, None, None)
  node_3 = TreeNode(3, node_1, node_2)

  expected_result = 2
  result = kth_smallest(node_3, 2)
  assert (result == expected_result)

  # Test case 2
  node_1 = TreeNode(1, None, None)
  node_2 = TreeNode(2, node_1, None)
  node_4 = TreeNode(4, None, None)
  node_3 = TreeNode(3, node_2, node_4)
  node_6 = TreeNode(6, None, None)
  node_5 = TreeNode(5, node_3, node_6)

  expected_result = 3
  result = kth_smallest(node_5, 3)
  assert (result == expected_result)
