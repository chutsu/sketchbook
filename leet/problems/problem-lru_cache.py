#!/usr/bin/env python3
"""
LeetCode 146. LRU Cache

Design a data structure that follows the constraints of a Least Recently Used
(LRU) cache. Implement the LRUCache class:

LRUCache(int capacity)
  Initialize the LRU cache with positive size capacity.

int get(int key)
  Return the value of the key if the key exists, otherwise return -1.

void put(int key, int value)
  Update the value of the key if the key exists. Otherwise, add the key-value
  pair to the cache. If the number of keys exceeds the capacity from this
  operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Example:

  LRUCache lRUCache = new LRUCache(2);
  lRUCache.put(1, 1); // cache is {1=1}
  lRUCache.put(2, 2); // cache is {1=1, 2=2}
  lRUCache.get(1);    // return 1
  lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
  lRUCache.get(2);    // returns -1 (not found)
  lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
  lRUCache.get(1);    // return -1 (not found)
  lRUCache.get(3);    // return 3
  lRUCache.get(4);    // return 4

"""

class Node:
  def __init__(self, key, value):
    self.next = None
    self.prev = None
    self.key = key
    self.value = value


class LRUCache:
  def __init__(self, capacity: int):
    # Cache properties
    self.cache = {}
    self.capacity = capacity
    self.size = 0

    # Left and right pointers
    # Left stores the least recent pointer
    # Right stores the most recent pointer
    self.left = Node(0, 0)
    self.right = Node(0, 0)
    self.left.next = self.right
    self.right.prev = self.left

  def _remove(self, node):
    # Remove node in the double linked list
    prev = node.prev
    nxt = node.next

    prev.next = nxt
    nxt.prev = prev

  def _insert(self, node):
    # Add node to the middle of the double linked list from the right
    prev = self.right.prev
    nxt = self.right

    prev.next = node
    nxt.prev = node

    node.next = nxt
    node.prev = prev

  def get(self, key: int) -> int:
    if key in self.cache:
      # Update double linked list
      self._remove(self.cache[key])
      self._insert(self.cache[key])

      # Return value
      return self.cache[key].value

    return -1

  def put(self, key: int, value: int) -> None:
    # Remove node from double linked list
    if key in self.cache:
      self._remove(self.cache[key])

    # Add to cache and insert node to double linked list
    self.cache[key] = Node(key, value)
    self._insert(self.cache[key])

    # Remove LRU
    if len(self.cache) > self.capacity:
      lru = self.left.next
      self._remove(lru)
      del self.cache[lru.key]
