#!/usr/bin/env python3
"""
LeetCode 1110: Delete nodes and return forest

Given the root of a binary tree, each node in the tree has a distinct value.
After deleting all nodes with a value in to_delete, we are left with a forest
(a disjoint union of trees). Return the roots of the trees in the remaining
forest. You may return the result in any order.

Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
"""

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def __repr__(self):
    return str(self.val)


def delete_nodes(root, to_delete):
  q = [(root, True)]
  res = []

  while q:
    node, new_root = q.pop(0)
    if new_root and node.val not in to_delete:
      res.append(node)

    new_root = node.val in to_delete
    if node.left:
      q.append((node.left, new_root))
      if node.left.val in to_delete:
        node.left = None

    if node.right:
      q.append((node.right, new_root))
      if node.right.val in to_delete:
        node.right = None

  return res


if __name__ == "__main__":
  node4 = TreeNode(4)
  node5 = TreeNode(5)
  node2 = TreeNode(2, node4, node5)
  node6 = TreeNode(6)
  node7 = TreeNode(7)
  node3 = TreeNode(3, node6, node7)
  node1 = TreeNode(1, node2, node3)

  res = delete_nodes(node1, [3,5])
  print(res)
