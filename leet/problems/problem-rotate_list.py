#!/usr/bin/env python3
"""
LeetCode 61: Rotate List

Given the head of a linked list, rotate the list to the right by k places.

-------------------------------------------------------------------------------

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

-------------------------------------------------------------------------------

Example 1:

Input: head = [0,1,2], k = 4
Output: [2,0,1]

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


def rotate_list(head, k):
  dummy = ListNode(0, head)

  # Go to last node
  length = 1
  end = head
  while end.next:
    end = end.next
    length += 1

  # Connect last to first node
  end.next = dummy.next

  # Go to start of rotated list
  i = length - (k % length)
  start = end
  for _ in range(i):
    start = start.next

  new_head = start.next
  start.next = None
  return new_head


if __name__ == "__main__":
  nums = [1, 2, 3, 4, 5]
  k = 2
  head = form_linked_list(nums)
  print_linked_list(head)
  new_head = rotate_list(head, k)
  print_linked_list(new_head)
