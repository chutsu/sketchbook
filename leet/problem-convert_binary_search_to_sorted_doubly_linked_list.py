#!/usr/bin/env python3
"""
LeetCode 426: Convert binary search tree to sorted circular doubly linked list

Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor
and successor pointers in a doubly-linked list. For a circular doubly linked
list, the predecessor of the first element is the last element, and the
successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left
pointer of the tree node should point to its predecessor, and the right pointer
should point to its successor. You should return the pointer to the smallest
element of the linked list.
"""

class TreeNode:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __repr__(self):
    return str(self.value)


def convert(root):
  # Get all the nodes in the tree via BST
  queue = [root]
  for node in queue:
    if node.left:
      queue.append(node.left)
    if node.right:
      queue.append(node.right)

  # Sort the nodes
  queue.sort(key=lambda n : n.value)

  # Fix the connections
  for i, node in enumerate(queue):
    if i == 0:
      node.left = queue[-1]
    else:
      node.left = queue[i - 1]

    if i == (len(queue) - 1):
      node.right = queue[0]
    else:
      node.right = queue[i + 1]

  # Return the head
  return queue[0]


if __name__ == "__main__":
  """
  Tree:
      4
    2   5
  1  3
  """
  n1 = TreeNode(1)
  n3 = TreeNode(3)
  n2 = TreeNode(2, n1, n3)
  n5 = TreeNode(5)
  n4 = TreeNode(4, n2, n5)

  head = convert(n4)
  for i in range(5):
    assert head.value == (i + 1)
    head = head.right
