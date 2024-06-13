#!/usr/bin/env python3
"""
LeetCode 2265: Count Nodes Equal to Average of Subtree

Given the root of a binary tree, return the number of nodes where the value of
the node is equal to the average of the values in its subtree.

Note:

- The average of n elements is the sum of the n elements divided by n and
  rounded down to the nearest integer.
- A subtree of root is a tree consisting of root and all of its descendants.
"""
class Node:
  def __init__(self, value = None, left = None, right = None):
    self.value = value
    self.left = left
    self.right = right


def find_count(node):
  if not node:
    return 0, 0, 0 # sum, count, ans

  left_sum, left_count, left_ans = find_count(node.left)
  right_sum, right_count, right_ans = find_count(node.right)

  s = left_sum + right_sum + node.value
  n = left_count + right_count + 1
  ans = left_ans + right_ans
  if int(s / n) == node.value:
    ans += 1

  return s, n, ans


if __name__ == "__main__":
  node0 = Node(0)
  node1 = Node(1)
  node8 = Node(8, node0, node1)
  node6 = Node(6)
  node5 = Node(5, None, node6)
  node4 = Node(4, node8, node5)

  assert find_count(node4)[2] == 5
