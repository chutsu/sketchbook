#!/usr/bin/env python3
"""
Dijkstra's algorithm
====================

Dijkstra's algorithm finds the shortest path from a given source node to every
other node. It can be used to find the shortest path to a specific destination
node, by terminating the algorithm after determining the shortest path to that
node.

"""
import heapq


def dijkstra(graph, start, goal):
  # Find shortest path
  parent = {node: None for node in graph}
  weights = {node: float('inf') for node in graph}
  weights[start] = 0
  pq = [(0, start)]

  while pq:
    w, u = heapq.heappop(pq)
    if w > weights[u]:
      continue

    if u == goal:
      break

    for v, weight in graph[u].items():
      w_new = w + weight
      if w_new < weights[v]:
        weights[v] = w_new
        parent[v] = u
        heapq.heappush(pq, (w_new, v))

  # Path Reconstruction
  path = []
  curr = goal
  while curr is not None:
    path.append(curr)
    curr = parent[curr]

  path.reverse()
  if path[0] != start:
    return None, float('inf')

  return path, weights[goal]


# --- Example Usage ---
graph = {
    'A': {
        'B': 4,
        'C': 2
    },
    'B': {
        'D': 3,
        'E': 1
    },
    'C': {
        'B': 1,
        'D': 5
    },
    'D': {
        'E': 1
    },
    'E': {},
}

path, cost = dijkstra(graph, 'A', 'E')
print(f"Shortest Path: {path} with total cost: {cost}")
# Output: Shortest Path: ['A', 'C', 'B', 'E'] with total cost: 4
