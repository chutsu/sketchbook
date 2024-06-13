#!/usr/bin/env python3


class TreeNode:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __str__(self):
    return str(self.value)

  def __repr__(self):
    return str(self.value)


def print_tree(root):
  if root is None:
    return

  level = 1
  queue = [(level, root)]
  output = []

  while len(queue):
    level, n = queue.pop(0)

    if len(output) != level:
      output.append([n])
    else:
      output[level - 1].append(n)
    level += 1

    if n.left:
      queue.append((level, n.left))
    if n.right:
      queue.append((level, n.right))

  print(output)


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


if __name__ == "__main__":
  node_1 = TreeNode(1)
  node_3 = TreeNode(3)
  node_2 = TreeNode(2, node_1, node_3)

  node_6 = TreeNode(6)
  node_9 = TreeNode(9)
  node_7 = TreeNode(7, node_6, node_9)

  node_4 = TreeNode(4, node_2, node_7)

  print_tree(node_4)
  print_tree(invert_binary_tree_iterative(node_4))
  print_tree(invert_binary_tree_recursive(node_4))
