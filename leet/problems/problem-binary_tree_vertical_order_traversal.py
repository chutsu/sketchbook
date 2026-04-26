#!/usr/bin/env python3
"""
LeetCode 314: Binary Tree Vertical Order Traversal

Given the root of a binary tree, return the vertical order traversal of its
nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to
right.
"""
import collections

class TreeNode:
  def __init__(self, value, left=None, right=None):
    self.left = left
    self.right = right
    self.value = value

  def __str__(self):
    return self.value

  def __repr__(self):
    return str(self.value)

def vertical_order_traversal(root):
  if root is None:
    return []

  columns = collections.defaultdict(list)
  q = [(root, 0)]
  while len(q):
    n, level = q.pop(0)
    columns[level].append(n)

    if n.left:
      q.append((n.left, level - 1))
    if n.right:
      q.append((n.right, level + 1))

  return [columns[level] for level in range(min(columns), max(columns) + 1)]


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

  results = vertical_order_traversal(n3)
  print(results)


  """
       3
    9     8
  4   0 1   7
  """
  n4 = TreeNode(4)
  n0 = TreeNode(0)
  n1 = TreeNode(1)
  n7 = TreeNode(7)
  n9 = TreeNode(9, n4, n0)
  n8 = TreeNode(8, n1, n7)
  n3 = TreeNode(3, n9, n8)

  results = vertical_order_traversal(n3)
  print(results)
