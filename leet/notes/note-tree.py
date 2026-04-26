#!/usr/bin/env python3
import numpy as np


class TreeNode:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right


class Tree:
  def __init__(self, root=None):
    self.root = root


def tree_dfs(node):
  if node.value is None:
    return

  print(node.value)

  if node.left:
    tree_dfs(node.left)

  if node.right:
    tree_dfs(node.right)


def tree_bfs_iterative(tree):
  queue = []
  queue.append(tree.root)

  while len(queue):
    node = queue.pop(0)
    print(node.value)

    if node.left:
      queue.append(node.left)
    if node.right:
      queue.append(node.right)


def tree_dfs_iterative(tree):
  stack = []
  stack.append(tree.root)

  while len(stack):
    node = stack.pop()

    print(node.value)

    # Note: to make the iterative DFS output the same as the recurisve DFS we
    # have swapped the order of which child node to be added to the stack
    # first. This, however, is not a requirement.
    if node.right:
      stack.append(node.right)

    if node.left:
      stack.append(node.left)


def tree_max_depth(node):
  if node is None:
    return 0

  return 1 + max(tree_max_depth(node.left), tree_max_depth(node.right))


def tree_min_depth(node):
  if node is None:
    return 0

  return 1 + min(tree_max_depth(node.left), tree_max_depth(node.right))


def invert_binary_tree_iterative(root):
  new_root = TreeNode(root.value)

  queue = [root]
  queue_new = [new_root]
  while len(queue):
    n = queue.pop(0)
    nn = queue_new.pop(0)

    if n.left:
      nn.right = TreeNode(n.left.value)
      queue.append(n.left)
      queue_new.append(nn.right)

    if n.right:
      nn.left = TreeNode(n.right.value)
      queue.append(n.right)
      queue_new.append(nn.left)

  return new_root


def invert_binary_tree_recursive(root):
  if root is None:
    return root

  invert_binary_tree_recursive(root.left)
  invert_binary_tree_recursive(root.right)

  tmp = root.left
  root.left = root.right
  root.right = tmp

  return root


def build_bst(arr):
  if not arr:
    return None

  N = len(arr)
  if N == 1:
    return TreeNode(arr[0], None, None)

  else:
    mid = int(len(arr) / 2)
    mid_node = TreeNode(arr[mid], None, None)
    mid_node.left = build_bst(arr[0:mid])
    mid_node.right = build_bst(arr[mid + 1:N])
    return mid_node


if __name__ == "__main__":
  # Tree:
  #        A
  #       / \
  #      B   C
  #         / \
  #        D   E
  #       /
  #       F
  F = TreeNode("F")
  D = TreeNode("D", F)
  E = TreeNode("E")
  C = TreeNode("C", D, E)
  B = TreeNode("B")
  A = TreeNode("A", B, C)
  t = Tree(A)

  # tree_dfs(A)
  # tree_bfs_iterative(t)
  # tree_dfs_iterative(t)
  # print(f"Max depth: {tree_max_depth(A)}")
  # print(f"Min depth: {tree_min_depth(A)}")
