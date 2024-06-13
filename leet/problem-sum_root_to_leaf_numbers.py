#!/usr/bin/env python3
"""
LeetCode 129: Sum Root to Leaf Numbers

You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

  For example, the root-to-leaf path 1->2->3 represents the number 123.

Return the total sum of all root-to-leaf numbers. Test cases are generated so
that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

------------------------------------------------------------------------------

Example 1:

Input:

  root: [1, 2, 3]

Output:

  25

Explanation:

  The root-to-leaf path 1->2 represents the number 12.
  The root-to-leaf path 1->3 represents the number 13.
  Therefore, sum = 12 + 13 = 25.

------------------------------------------------------------------------------

Example 2:

Input:

  root = [4,9,0,5,1]

      4
    9    0
  5   1


Output:

  1026

Explanation:

  The root-to-leaf path 4->9->5 represents the number 495.
  The root-to-leaf path 4->9->1 represents the number 491.
  The root-to-leaf path 4->0 represents the number 40.
  Therefore, sum = 495 + 491 + 40 = 1026.

"""


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def sum_root_to_leaf(root):
  root_to_leaf = 0
  stack = [(root, 0)]

  while len(stack):
    node, num = stack.pop(-1)
    num = num * 10 + node.val

    if not node.left and not node.right:
      root_to_leaf += num

    if node.left:
      stack.append((node.left, num))
    if node.right:
      stack.append((node.right, num))

  return root_to_leaf

if __name__ == "__main__":
  node1 = TreeNode(1)
  node5 = TreeNode(5)
  node9 = TreeNode(9, node5, node1)
  node0 = TreeNode(0)
  node4 = TreeNode(4, node9, node0)

  print(sum_root_to_leaf(node4))



