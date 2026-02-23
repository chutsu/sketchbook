#!/usr/bin/env python3
"""
Kahn’s Algorithm
================

Kahn’s Algorithm is a method for producing a topological sort of a Directed
Acyclic Graph (DAG) by iteratively removing nodes with an indegree of zero. It
starts by placing all nodes that have no incoming edges into a queue; as each
node is removed and added to the sorted list, the algorithm "deletes" its
outgoing edges, updating the indegrees of its neighbors. Any neighbor whose
indegree drops to zero is then added to the queue. If all nodes are processed,
the sort is complete; if any nodes remain, the graph contains a cycle, making a
topological ordering impossible.

"""
from collections import defaultdict


def kahn(num_nodes, dependencies):
  # Build the graph and calculate in-degrees
  adj_list = defaultdict(list)
  in_degree = defaultdict(int)
  for prereq, src in dependencies:
    adj_list[prereq].append(src)
    in_degree[src] += 1

  # Add all nodes with in-degree 0 to the queue
  queue = []
  for i in range(num_nodes):
    if in_degree[i] == 0:
      queue.append(i)

  # Traverse graph (starting nodes with 0 deps)
  topo_order = []
  while queue:
    u = queue.pop(0)
    topo_order.append(u)

    for v in adj_list[u]:
      in_degree[v] -= 1
      if in_degree[v] == 0:
        queue.append(v)

  # Check for cycles
  if len(topo_order) == num_nodes:
    return topo_order[::-1]

  return [] # Detected cycle


if __name__ == "__main__":
  # 5 nodes: 0, 1, 2, 3, 4
  # Edges: (0->1), (0->2), (1->3), (2->3), (3->4)
  # 0 -> 1 -> 3 -> 4
  # |--> 2 ---^
  num_nodes = 5
  dependencies = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]
  topo_order = kahn_topological_sort(num_nodes, dependencies)
  print(topo_order)
