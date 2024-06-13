#!/usr/bin/env/python3
"""
LeetCode 2: Add Two Numbers

You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order, and each of their nodes
contains a single digit. Add the two numbers and return the sum as a linked
list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

-------------------------------------------------------------------------------

Example 1:

Input:

  l1 = [2,4,3], l2 = [5,6,4]

Output:

  [7,0,8]

Explanation: 342 + 465 = 807.

-------------------------------------------------------------------------------

Example 2:

Input:

  l1 = [0], l2 = [0]

Output: [0]

-------------------------------------------------------------------------------

Example 3:

Input:

  l1 = [9,9,9,9,9,9,9],
  l2 = [9,9,9,9]

Output:

  [8,9,9,9,0,0,0,1]

"""

class ListNode:
  def __init__(self, val, next_node=None):
    self.val = val
    self.next = next_node


def add_two_numbers(l1, l2):
  dummy = ListNode(0)
  node = dummy.next


if __name__ == "__main__":
  node3 = ListNode(3)
  node4 = ListNode(4, node3)
  node2 = ListNode(2, node4)
  l1 = node2

  node5 = ListNode(5)
  node6 = ListNode(6, node5)
  node4 = ListNode(4, node6)
  l2 = node4



