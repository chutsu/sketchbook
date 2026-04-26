#!/usr/bin/env python3
"""
LeetCode 621: Task Scheduler
----------------------------

Given a characters array tasks, representing the tasks a CPU needs to do, where
each letter represents a different task. Tasks could be done in any order. Each
task is done in one unit of time. For each unit of time, the CPU could complete
either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period
between two same tasks (the same letter in the array), that is that there must
be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all
the given tasks.

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8

Explanation:
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
"""
from collections import Counter
import heapq


def least_interval(tasks, n):
  # Get frequency counts of each task and order it based on frequency
  # Note: When creating the heap, counts are multiplied by -1 because python only
  # has a min-heap implementation
  counts = Counter(tasks)
  max_heap = [-1 * c for c in counts.values()]
  heapq.heapify(max_heap)

  # The idea is to:
  # 1. simulate a queue with (task, time_limit) pairs in the queue.
  # 2. Push the the most frequent tasks first

  time = 0
  q = []
  while len(max_heap) or len(q):
    # Do we still have tasks?
    if len(max_heap):
      count = 1 + heapq.heappop(max_heap)
      if count:
        q.append([count, time + n])

    # Can we empty the task queue?
    if len(q) and q[0][1] == time:
      heapq.heappush(max_heap, q.pop(0)[0])
      # ^ Push the task back to the heap

    # Update time
    time += 1

  return time


if __name__ == "__main__":
  tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
  n = 2
  time = least_interval(tasks, n)
  print(time)
