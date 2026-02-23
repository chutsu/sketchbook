#!/usr/bin/env python3
"""
LeetCode 210: Course Schedule II

There are a total of numCourses courses you have to take, labeled from 0 to
numCourses - 1. You are given an array prerequisites where prerequisites[i] =
[ai, bi] indicates that you must take course bi first if you want to take
course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to
first take course 1.

Return the ordering of courses you should take to finish all courses. If there
are many valid answers, return any of them. If it is impossible to finish all
courses, return an empty array.
"""
from collections import defaultdict


def solution(num_courses, prerequisites):
  premap = defaultdict(list)
  for crs, prereq in prerequisites:
    premap[crs].append(prereq)


  def dfs(premap, crs, cycle, path, res):
    if crs in cycle:
      return False

    if crs in path:
      return True

    cycle.add(crs)
    for c in premap[crs]:
      if dfs(premap, c, cycle, path, res) is False:
        return False
    cycle.remove(crs)

    path.add(crs)
    res.append(crs)

    return True

  cycle = set()
  path = set()
  res = []
  for crs in range(num_courses):
    if dfs(premap, crs, cycle, path, res) is False:
      return []

  return res


if __name__ == "__main__":
  num_courses = 5
  prerequisites = [(0, 1), (0, 2), (1, 3), (1, 4), (3, 4)]
  print(solution(num_courses, prerequisites))
