#!/usr/bin/env python3
# LeetCode 118: Pascal's Triangle [Easy]

def pascals_triangle(num_rows):
  # Edge cases
  if num_rows == 0:
    return []
  if num_rows == 1:
    return [[1]]

  # Dynamically generate previous rows
  prev_rows = self.generate(num_rows - 1)
  prev_row = prev_rows[-1]

  # Current row
  current_row = []

  # -- Add left most value
  current_row.append(1)

  # -- Add values in the middle
  for i in range(1, num_rows - 1):
    current_row.append(prev_row[i - 1] + prev_row[i])

  # -- Add right most value
  current_row.append(1)

  # Return results
  prev_rows.append(current_row)
  return prev_rows


if __name__ == "__main__":
  pascals_triangle(5)
