#!/usr/bin/env python3
"""
LeetCode 2385: Amount of time for binary tree to be infected

You are given the root of a binary tree with unique values, and an integer
start. At minute 0, an infection starts from the node with value start.

Each minute, a node becomes infected if:

    The node is currently uninfected.
    The node is adjacent to an infected node.

Return the number of minutes needed for the entire tree to be infected.

Example:

Input:

  root = [1,5,3,null,4,10,6,9,2],
  start = 3

            1
        5       3
          4   10  6
        9   2

Output: 4

Explanation: The following nodes are infected during:
- Minute 0: Node 3
- Minute 1: Nodes 1, 10 and 6
- Minute 2: Node 5
- Minute 3: Node 4
- Minute 4: Nodes 9 and 2
It takes 4 minutes for the whole tree to be infected so we return 4.
"""
import collections

class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def infection_time(root, start):
  def create_graph(node, graph):
    if node is None:
      return

    if node.left:
      graph[node.val].append(node.left.val)
      graph[node.left.val].append(node.val)
      create_graph(node.left, graph)

    if node.right:
      graph[node.val].append(node.right.val)
      graph[node.right.val].append(node.val)
      create_graph(node.right, graph)

  graph = collections.defaultdict(list)
  create_graph(root, graph)
  q = [(start, 0)] # Start node value, minutes
  visited = set()
  ans = 0

  while len(q):
    val, minute = q.pop(0)
    ans = max(ans, minute)
    visited.add(val)

    for neighbour in graph[val]:
      if neighbour not in visited:
        q.append((neighbour, minute + 1))

  return ans


if __name__ == "__main__":
  node2 = Node(2)
  node9 = Node(9)
  node4 = Node(4, node9, node2)
  node5 = Node(5, None, node4)
  node10 = Node(10)
  node6 = Node(6)
  node3 = Node(3, node10, node6)
  node1 = Node(1, node5, node3)

  start = 3
  assert infection_time(node1, start) == 4
