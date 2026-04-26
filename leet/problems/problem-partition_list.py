#!/usr/bin/env python3
"""
LeetCode 86: Partition List

Given the head of a linked list and a value x, partition it such that all nodes
less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two
partitions.

-------------------------------------------------------------------------------

Example 1:

Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

-------------------------------------------------------------------------------

Example 2:

Input: head = [2,1], x = 2
Output: [1,2]

"""

class ListNode:
  def __init__(self, val=0, next_node=None):
    self.val = val
    self.next = next_node


def form_linked_list(nums):
  dummy = ListNode()
  curr = dummy
  for num in nums:
    curr.next = ListNode(num)
    curr = curr.next
  return dummy.next


def print_linked_list(head):
  node = head
  while node:
    print(f"{node.val} ", end="")
    node = node.next
  print("")


def partition_list(head, x):
  left_head = ListNode()
  right_head = ListNode()
  left = left_head
  right = right_head

  curr = head
  while curr:
    if curr.val < x:
      left.next = curr
      left = left.next
    else:
      right.next = curr
      right = right.next
    curr = curr.next

  left.next = right_head.next
  right.next = None
  return left_head.next


if __name__ == "__main__":
  nums = [1, 4, 3, 2, 5, 2]
  x = 3
  head = form_linked_list(nums)

  print_linked_list(head)
  partition_list(head, x)
  print_linked_list(head)
