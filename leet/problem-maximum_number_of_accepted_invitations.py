#!/usr/bin/env python3
"""
LeetCode 1820: Maximum Number of Accepted Invitations

There are m boys and n girls in a class attending an upcoming party.

You are given an m x n integer matrix grid, where grid[i][j] equals 0 or 1. If
grid[i][j] == 1, then that means the ith boy can invite the jth girl to the
party. A boy can invite at most one girl, and a girl can accept at most one
invitation from a boy.

Return the maximum possible number of accepted invitations.

Example 1:

Input: grid = [[1,1,1],
               [1,0,1],
               [0,0,1]]
Output: 3

Explanation: The invitations are sent as follows:
- The 1st boy invites the 2nd girl.
- The 2nd boy invites the 1st girl.
- The 3rd boy invites the 3rd girl.


Example 2:

Input: grid = [[1,0,1,0],
               [1,0,0,0],
               [0,0,1,0],
               [1,1,1,0]]
Output: 3
Explanation: The invitations are sent as follows:
-The 1st boy invites the 3rd girl.
-The 2nd boy invites the 1st girl.
-The 3rd boy invites no one.
-The 4th boy invites the 2nd girl.
"""

def max_invitations(grid):
  M = len(grid)
  N = len(grid[0])
  matches = {}

  def find(i, visited):
    for j in range(N):
      # No invitation
      if grid[i][j] == 0:
        continue

      # Processed already
      if j in visited:
        continue

      # 1. Girl has no invitation
      # 2. Girl has invitation but boy can find another girl
      visited.add(j)
      if j not in matches or find(matches[j], visited):
        matches[j] = i
        return True

    return False

  for i in range(M):
    find(i, set())

  return len(matches)

if __name__ == "__main__":
  grid = [[1, 0, 1, 0], [1, 0, 0, 0], [0, 0, 1, 0], [1, 1, 1, 0]]
  assert max_invitations(grid) == 3
