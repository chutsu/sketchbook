#!/usr/bin/env python3


class ListNode:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next = next_node

  def __str__(self):
    return str(self.value)

  def __repr__(self):
    return self.value


def print_list(head):
  node = head
  while node:
    print(node, end=" ")
    node = node.next
  print()


def remove_elements(head, target):
  if head is None:
    return head

  tmp = ListNode()
  tmp.next = head
  node = tmp

  while node.next:
    if node.next.value == target:
      node.next = node.next.next
    else:
      node = node.next

  return tmp.next


if __name__ == "__main__":
  # Setup linked list: [1, 2, 6, 3, 4, 5, 6]
  node_list = [1, 2, 6, 3, 4, 5, 6]
  head = ListNode(node_list[0], None)
  node = head
  for i, num in enumerate(node_list[1:]):
    node.next = ListNode(num)
    node = node.next

  # Before remove
  print("Before Remove")
  print_list(head)
  print()

  # Remove
  target = 6
  print(f"Removing {target}")
  head = remove_elements(head, target)
  print()

  # After remove
  print("After Remove")
  print_list(head)
