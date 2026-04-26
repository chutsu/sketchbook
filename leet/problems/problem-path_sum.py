#!/usr/bin/env python3
# LeetCode 112: Path Sum [Medium]


def dfs(node, target_sum, target_paths, path):
  if node is None:
    return

  # Leaf node?
  if node.left is None and node.right is None:
    # Sum path
    s = 0
    for node in path:
      s += node.val

    # Add to target paths
    if s == target_sum:
      target_paths.append(path)

    return

  # Traverse left paths
  if node.left:
    dfs(node.left, target_sum, target_paths, path + [node.left])

  # Traverse right paths
  if node.right:
    dfs(node.right, target_sum, target_paths, path + [node.right])


def has_path_sum(root, target_sum):
  target_paths = []
  dfs(root, target_sum, target_paths, [root])
  return len(target_paths)
