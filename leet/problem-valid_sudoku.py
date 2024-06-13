#!/usr/bin/env python3


def check_row(board, row_index):
  counter = [0] * 9
  for number in board[row_index]:
    if number == ".":
      continue

    number = int(number)
    if counter[number - 1] == 1:
      return False
    counter[number - 1] = 1

  return True


def check_column(board, col_index):
  counter = [0] * 9
  for row in board:
    if row[col_index] == ".":
      continue

    number = int(row[col_index])
    if counter[number - 1] == 1:
      return False
    counter[number - 1] = 1

  return True


def check_cell(board, row_start, col_start):
  counter = [0] * 9
  for i in range(row_start, row_start + 3):
    for j in range(col_start, col_start + 3):
      if board[i][j] == ".":
        continue

      number = int(board[i][j])
      if counter[number - 1] == 1:
        return False
      counter[number - 1] = 1

  return True


def is_valid_sudoku(board):
  num_rows = 9
  num_cols = 9

  for i in range(num_rows):
    if check_row(board, i) is False:
      return False

  for i in range(num_cols):
    if check_column(board, i) is False:
      return False

  for row_start in range(0, num_rows, 3):
    for col_start in range(0, num_cols, 3):
      if check_cell(board, row_start, col_start) is False:
        return False

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
