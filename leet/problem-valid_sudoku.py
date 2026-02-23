#!/usr/bin/env python3
"""
LeetCode 36: Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9
    without repetition.

Note:

    A Sudoku board (partially filled) could be valid but is not necessarily
    solvable. Only the filled cells need to be validated according to the
    mentioned rules.

"""
from collections import defaultdict

def is_valid_sudoku(board):
  rows = defaultdict(set)
  cols = defaultdict(set)
  squares = defaultdict(set)

  for r in range(9):
    for c in range(9):
      if board[r][c] == ".":
        continue

      x = board[r][c]
      if x in rows[r] or x in cols[r] or x in squares[(r // 3, c // 3)]:
        return False

      rows[r].add(x)
      cols[c].add(x)
      squares[(r // 3, c // 3)].add(x)

  return True


if __name__ == "__main__":
  valid_board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
                 ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                 [".", "9", "8", ".", ".", ".", ".", "6", "."],
                 ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                 ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                 ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                 [".", "6", ".", ".", ".", ".", "2", "8", "."],
                 [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                 [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
  assert (is_valid_sudoku(valid_board) is True)

  invalid_board = [["8", "3", ".", ".", "7", ".", ".", ".", "."],
                   ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                   [".", "9", "8", ".", ".", ".", ".", "6", "."],
                   ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                   ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                   ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                   [".", "6", ".", ".", ".", ".", "2", "8", "."],
                   [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                   [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
  assert (is_valid_sudoku(invalid_board) is False)
