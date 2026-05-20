#!/usr/bin/env python3
"""
# Depth first search (DFS)

DFS stand for "Depth First Search", it starts the traversal from the root node
and explore the search as far as possible from the root node, i.e. depth wise.

          A
         / \
        B   C
       /   / \
      D   E   F

    A, B, D, C, E, F

DFS can be done with the help of a `STACK` (LIFO) implementation. The algorithm
works in two stages, in teh first stage the visited vertices are pushed onto
the stack, and alter on when there is no vertex further to visite those are
popped off.

DFS is faster than BFS and requires less memeory compared to BFS.

Applications of DFS include:

- Cycle detection
- Connectivity testing
- Finding a path between V and W in the graph
- Useful in finding spanning trees & forest

The disavange of using DFS is that it is not so useful in finding the shortest
path. It is uesd to perfrom a traversal of a general graph and the idea of DFS
is to make a path as long as possible and backtrack to add branches also as
long as possible.


# Breadth First Search (BFS)

BFS stand for "Breadth First Search", starts traversal from the root node and
then explore the search in the level by level manner, i.e. as close as possible
from the root node.

BFS can be done with the help of a `QUEUE` (FIFO) implementation. This algorithm
works in single stage. The visited vertices are removed from the queue and then
displayed at once.

BFS is slower than DFS and requires more memory.

Applications of BFS includes:
- Finding the shortest path
- Single source and All pairs of shortest paths
- Spanning Tree
- In connectivity


          A
         / \
        B   C
       /   / \
      D   E   F

    A, B, C, D, E, F



# Iterative Deepening Depth First Search (IDDFS)

Iterative Deepening Depth First Search (IDDFS) is a state space search strategy
in which a depth-limited search is run repeatedly, increasing the depth limit
with each iteration until it reaches `d`, the depth of the shallowest goal
state. IDDFS is equivalent to BFS, but uses much less memory; on each
iteration, it visits the nodes in the search tree in the same order as depth
first search, but the cumulative order in which the nodes are first visited is
effectively breadth-first.

IDDFS combines DFS's space efficiency and BFS's completeness (when branching
factor is finite). It is optimal when the path cost is a non-decreasing
function of the depth of the node. It may seem wasteful at first that IDDFS
visits states multiple times, but this is not the case, since in a tree most of
the nodes are in the bottom level, so it does not matter much if the upper
levels are visited multiple times.
"""

def binary_search(nums, target):
  left = 0
  right = len(nums) - 1

  while left <= right:
    mid = left + int((right - left) / 2)

    if nums[mid] == target:
      return mid

    elif nums[mid] > target:
      right = mid - 1

    else:
      left = mid + 1

  return -1


def binary_search_rotated_list(nums, target):
  left = 0
  right = len(nums) - 1

  while left <= right:
    mid = left + int((right - left) / 2)

    if nums[mid] == target:
      return mid

    if nums[mid] < nums[right]:
      if nums[mid] < target and target <= nums[right]:
        left = mid + 1
      else:
        right = mid - 1

    else:
      if nums[left] <= target and target < nums[mid]:
        right = mid - 1
      else:
        left = mid + 1

  return -1


if __name__ == "__main__":
  # Standard binary search
  nums = [1, 2, 3, 4, 5, 6, 7]
  index = binary_search(nums, 6)
  assert (index == 5)
  index = binary_search(nums, 2)
  assert (index == 1)

  # Perform binary search on a potentially pivoted sorted list
  nums = [4, 5, 6, 7, 0, 1, 2]
  target = 0
  index = binary_search_rotated_list(nums, target)
  assert (index == 4)
