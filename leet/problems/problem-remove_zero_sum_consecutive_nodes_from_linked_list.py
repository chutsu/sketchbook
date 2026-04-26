#!/usr/bin/env python3
"""
LeetCode 1171: Remove Zero Sum Consecutive Nodes from Linked List
Given the head of a linked list, we repeatedly delete consecutive sequences of
nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any
such answer.

(Note that in the examples below, all sequences are serializations of ListNode
objects.)

-------------------------------------------------------------------------------

Example 1:

  Input: head = [1,2,-3,3,1]

Output:

  [3,1]

Note: The answer [1,2,1] would also be accepted.

-------------------------------------------------------------------------------

Example 2:

Input: head = [1,2,3,-3,4]
Output: [1,2,4]

-------------------------------------------------------------------------------

Example 3:

  Input: head = [1,2,3,-3,-2]

Output: [1]

"""

class ListNode:
  def __init__(self, val, next_node=None):
    self.val = val
    self.next = next_node


def remove_zero_sum_nodes(head):
  dummy = ListNode(0, head)
  mp = {0: dummy}

  # Create a prefix sum map
  prefix_sum = 0
  while head:
    prefix_sum += head.val
    mp[prefix_sum] = head
    head = head.next

  # Loop through prefix sum map
  head = dummy
  prefix_sum = 0
  while head:
    prefix_sum += head.val
    head.next = mp[prefix_sum].next
    head = head.next

  return dummy.next


def removeZeroSumSublists(head):
  dummy = ListNode(0, head)
  pre = 0
  mp = {0: dummy}

  # Build map of prefix sum to node
  while head:
    pre += head.val
    mp[pre] = head
    head = head.next

  # Remove
  head = dummy
  pre = 0
  while head:
    pre += head.val
    head.next = mp[pre].next
    head = head.next

  return dummy.next


def extract_values(head):
  results = []
  while head:
    results.append(head.val)
    head = head.next
  return results


if __name__ == "__main__":
  node_m2 = ListNode(-2)
  node_m3 = ListNode(-3, node_m2)
  node_3 = ListNode(3, node_m3)
  node_2 = ListNode(2, node_3)
  node_1 = ListNode(1, node_2)

  head = remove_zero_sum_nodes(node_1)
  values = extract_values(head)
  print(values)
  assert values == [1]
