#!/usr/bin/env python3


class ListNode:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next = next_node

  def __str__(self):
    return str(self.value)

  def __repr__(self):
    return self.value


def remove_target(head, target):
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


def has_loop(head):
  tortoise = head
  hare = head

  while tortoise is not None or hare is not None:
    tortoise = tortoise.next
    hare = hare.next.next
    if tortoise == hare:
      return True

  return False


def get_loop_start(head):
  tortoise = head
  hare = head

  # Check if there's a loop
  while tortoise is not None or hare is not None:
    tortoise = tortoise.next
    hare = hare.next.next
    if tortoise == hare:
      break

  # No loop
  if hare.next is None:
    return None

  # Find where the loop starts
  n1 = head
  n2 = hare
  while n1 is not n2:
    n1 = n1.next
    n2 = n2.next
  return n2


def reverse_list(head):
  curr = head
  prev = None

  while curr:
    next_node = curr.next
    curr.next = prev

    prev = curr
    curr = next_node

  return prev


def print_list(head):
  node = head
  while node:
    print(f"{node.value} ", end="")
    node = node.next
  print()


if __name__ == "__main__":
  node_list = [1, 2, 6, 3, 4, 5, 6]
  head = ListNode(node_list[0], None)
  node = head
  for i, num in enumerate(node_list[1:]):
    node.next = ListNode(num)
    node = node.next

  print_list(head)
  remove_target(head, 6)
  print_list(head)
