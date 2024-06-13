#!/usr/bin/env python3
import sys

"""
Heap data structure is a complete binary tree that satisfies the heap property,
where any given node is always greater than its child node(s) and the key of
the root node is the largest among all other nodes. This is the max-heap
property. The opposite is a min-heap property.
"""

class Heap:
  def __init__(self, capacity):
    self.capacity = capacity
    self.size = 0
    self.heap = [-1 * sys.maxsize] * (self.capacity + 1)
    self.front = 1

  def _parent(self, index):
    return int(index / 2)

  def _left(self, index):
    return 2 * index

  def _right(self, index):
    return (2 * index) + 1

  def _is_leaf(self, index):
    return (index * 2) > self.size

  def _swap(self, src_index, dst_index):
    tmp = self.heap[dst_index]
    self.heap[dst_index] = self.heap[src_index]
    self.heap[src_index] = tmp

  def _heapify(self, index):
    # Pre-check
    if self._is_leaf(index):
      return

    if not (self.heap[index] > self.heap[self._left(index)] or
            self.heap[index] > self.heap[self._right(index)]):
      return

    if self.heap[self._left(index)] < self.heap[self._right(index)]:
      self._swap(index, self._left(index))
      self._heapify(self._left(index))
    else:
      self._swap(index, self._right(index))
      self._heapify(self._right(index))

  def min_heap(self):
    for index in range(int(self.size / 2), 0, -1):
      self._heapify(index)

  def insert(self, value):
    # Check if capacity is reached
    if self.size >= self.capacity:
      return

    # Add to heap
    self.size += 1
    self.heap[self.size] = value

    # Reorder heap (bubble the min to the top)
    index = self.size
    while self.heap[index] < self.heap[self._parent(index)]:
      self._swap(index, self._parent(index))
      index = self._parent(index)
      print(f"swap {index}, {self._parent(index)}, heap: {self.heap}")


if __name__ == "__main__":
  data = [17, 5, 3, 10, 84, 19, 6, 22, 9]
  heap = Heap(5)
  heap.insert(data[0])
  heap.insert(data[1])
  heap.insert(data[2])
  heap.min_heap()
  # print(heap.heap)
