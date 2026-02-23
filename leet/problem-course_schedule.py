#!/usr/bin/env python3
"""
LeetCode 207: Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to
`numCourses - 1`. You are given an array prerequisites where `prerequisites[i]
= [ai, bi]` indicates that you must take course `bi` first if you want to take
course `ai`.

For example, the pair [0, 1], indicates that to take course 0 you have to first
take course 1.

Return true if you can finish all courses. Otherwise, return false.
"""
from collections import defaultdict


def solution(num_courses, prerequisites):
  premap = defaultdict(list)
  for crs, prereq in prerequisites:
    premap[crs].append(prereq)


  def dfs(premap, crs, cycle):
    if crs in cycle:
      return False

    cycle.add(crs)
    for c in premap[crs]:
      if dfs(premap, c, cycle) is False:
        return False
    cycle.remove(crs)

    return True

  cycle = set()
  for crs in range(num_courses):
    if dfs(premap, crs, cycle) is False:
      return False

  return True


if __name__ == "__main__":
  num_courses = 5
  prerequisites = [(0, 1), (0, 2), (1, 3), (1, 4), (3, 4)]
  assert solution(num_courses, prerequisites) is True
