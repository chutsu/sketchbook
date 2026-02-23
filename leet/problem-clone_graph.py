#!/usr/bin/env python3
"""
LeetCode 133: Clone Graph

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its
neighbors.

class Node {
  public int val;
  public List<Node> neighbors;
}

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed).
For example, the first node with val == 1, the second node with val == 2, and
so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite
graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the
copy of the given node as a reference to the cloned graph.
"""
from collections import deque


class Node:
  def __init__(self, val, neighbors):
    self.val = val
    self.neighbors = neighbors


def clone_graph(node):
  if not node:
    return node

  q = deque([node])
  clones = {node.val: Node(node.val, [])}
  while q:
    cur = q.popleft()
    cur_clone = clones[cur.val]

    for neighbor in cur.neighbors:
      if neighbor.val not in clones:
        clones[neighbor.val] = Node(neighbor.val, [])
        q.append(neighbor)

      cur_clone.neighbors.append(clones[neighbor.val])

  return clones[node.val]


if __name__ == "__main__":
  # adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
  # output = [[2, 4], [1, 3], [2, 4], [1, 3]]
  # clone_graph(
  pass
