#!/usr/bin/env python3
"""
LeetCode 380: Insert Delete GetRandom O(1)

Implement the RandomizedSet class:

RandomizedSet()
  Initializes the RandomizedSet object.

bool insert(int val)
  Inserts an item val into the set if not present. Returns true if the item was
  not present, false otherwise.

bool remove(int val)

  Removes an item val from the set if present. Returns true if the item was
  present, false otherwise.

int getRandom()

  Returns a random element from the current set of elements (it's guaranteed that
  at least one element exists when this method is called). Each element must have
  the same probability of being returned.

You must implement the functions of the class such that each function works in
average O(1) time complexity.
"""
import random


class RandomizedSet():
  def __init__(self):
    self.index_map = {}
    self.data = []

  def insert(self, val):
    if val in self.index_map:
      return False

    self.data.append(val)
    self.index_map[val] = len(self.data) - 1
    return True

  def remove(self, val):
    """
    The trick is to swap the value to be deleted with the last value
    in self.data and update the indicies.

    For Example, if we wanted to delete 3 in self.data:

      self.data = [0, 2, 3, 4, 8]
      self.index_map = {
        0: 0,
        2: 1,
        3: 2,
        4: 3,
        8: 4
      }

    We would get the last value which is 8 and swap it with 3

      self.data = [0, 2, 8, 4, 3]
      self.index_map = {
        0: 0,
        2: 1,
        3: 4,
        4: 3,
        8: 2
      }

    Update indicies in self.index_map and then pop the last value off.

      self.data = [0, 2, 8, 4]
      self.index_map = {
        0: 0,
        2: 1,
        4: 3,
        8: 2
      }

    """
    if val not in self.index_map:
      return False

    # Get the last value in self.data and also the index of `val`
    last_val = self.data[-1]
    val_index = self.index_map[val]

    # Swap the last value in self.data with `val` and update indices
    self.data[-1] = val
    self.data[val_index] = last_val
    self.index_map[last_val] = val_index

    # Pop the last value in self.data which is `val` and update indicies
    self.data.pop(-1)
    self.index_map.pop(val)

    return True

  def getRandom(self):
    return random.choice(self.data)


randset = RandomizedSet()
assert randset.insert(1) == True
assert randset.remove(2) == False
assert randset.insert(2) == True
randset.getRandom()
assert randset.remove(1) == True
assert randset.insert(2) == False
randset.getRandom()
