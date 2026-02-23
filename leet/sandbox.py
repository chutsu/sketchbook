import heapq


def dijkstra(graph, start, goal):
  parents = {node: None for node in graph}
  weights = {node: float("inf") for node in graph}
  weights[start] = 0
  pq = [(0, start)]

  while pq:
    w, u = heapq.heappop(pq)
    if w > weights[u]:
      continue

    if u == goal:
      break

    for v, w_i in graph[u].items():
      w_new = w + w_i
      if w_new < weights[v]:
        weights[v] = w_new
        parents[v] = u
        heapq.heappush(pq, (w_new, v))

  path = []
  curr = goal
  while curr:
    path.append(curr)
    curr = parents[curr]
  path.reverse()

  if path[0] != start:
    return None, float("inf")
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
