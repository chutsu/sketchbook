#!/usr/bin/env python3
"""
LeetCode 235: Lowest Common Ancestor of a Binary Search Tree

Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

Each node will have a reference to its parent node. The definition for Node is below:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}

According to the definition of LCA on Wikipedia: "The lowest common ancestor of
two nodes p and q in a tree T is the lowest node that has both p and q as
descendants (where we allow a node to be a descendant of itself)."
"""


class TreeNode:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.parent = None
    self.left = left
    self.right = right


def lowest_common_ancestor(p, q):
  path = set()

  while p:
    path.add(p)
    p = p.parent

  while q is not None and q not in path:
    q = q.parent

  return q

if __name__ == "__main__":
  """
  Tree:
       3
    5     1
   6 2   0 8
    7 4
  """
  n7 = TreeNode(7)
  n4 = TreeNode(4)
  n2 = TreeNode(2, n7, n4)
  n6 = TreeNode(6)
  n5 = TreeNode(5, n6, n2)
  n0 = TreeNode(0)
  n8 = TreeNode(8)
  n1 = TreeNode(1, n0, n8)
  n3 = TreeNode(3, n5, n1)

  n5.parent = n3
  n1.parent = n3
  n6.parent = n5
  n2.parent = n5
  n0.parent = n1
  n8.parent = n1
  n7.parent = n2
  n4.parent = n2

  assert lowest_common_ancestor(n5, n1).value == 3
  assert lowest_common_ancestor(n5, n4).value == 5
  assert lowest_common_ancestor(n6, n8).value == 3
  assert lowest_common_ancestor(n7, n4).value == 2
