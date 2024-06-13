#!/usr/bin/env python3
"""
LeetCode 105: Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where preorder is the preorder
traversal of a binary tree and inorder is the inorder traversal of the same
tree, construct and return the binary tree.
"""


class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def print_tree(root):
  q = [(0, root)]

  level_curr = 0
  while len(q):
    level, n = q.pop(0)

    if level != level_curr:
      print()
      level_curr = level
    print(n.val, end=" ")

    if n.left:
      q.append((level + 1, n.left))

    if n.right:
      q.append((level + 1, n.right))


def build_tree(preorder, inorder):
  if not preorder or not inorder:
    return None

  root = TreeNode(preorder[0])
  mid = inorder.index(preorder[0])
  root.left = build_tree(preorder[1:mid + 1], inorder[:mid])
  root.right = build_tree(preorder[mid + 1:], inorder[mid + 1:])
  return root


if __name__ == "__main__":
  preorder = [3, 9, 20, 15, 7]
  inorder = [9, 3, 15, 20, 7]
  tree = build_tree(preorder, inorder)
  print_tree(tree)
