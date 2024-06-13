#!/usr/bin/env python3
"""
LeetCode 733: Flood Fill

An image is represented by an m x n integer grid image where image[i][j]
represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood
fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected
4-directionally to the starting pixel of the same color as the starting pixel,
plus any pixels connected 4-directionally to those pixels (also with the same
color), and so on. Replace the color of all of the aforementioned pixels with
color.

Return the modified image after performing the flood fill.
"""


def flood_fill(screen, r, c, old_color, new_color):
  # Check boundaries
  if r < 0 or r >= len(screen):
    return
  if c < 0 or c >= len(screen[0]):
    return

  # Not old color
  if screen[r][c] != old_color:
    return

  # Already visited
  if screen[r][c] == new_color:
    return

  # Set new color
  screen[r][c] = new_color

  # Recursively fill colors
  flood_fill(screen, r + 1, c, old_color, new_color)
  flood_fill(screen, r - 1, c, old_color, new_color)
  flood_fill(screen, r, c + 1, old_color, new_color)
  flood_fill(screen, r, c - 1, old_color, new_color)


if __name__ == "__main__":
  screen = [
      [1, 1, 1, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1, 1, 0, 0],
      [1, 0, 0, 1, 1, 0, 1, 1],
      [1, 2, 2, 2, 2, 0, 1, 0],
      [1, 1, 1, 2, 2, 0, 1, 0],
      [1, 1, 1, 2, 2, 2, 2, 0],
      [1, 1, 1, 1, 1, 2, 1, 1],
      [1, 1, 1, 1, 1, 2, 2, 1],
  ]

  print("Before Flood-Fill:")
  for row in screen:
    print(row)
  print()

  r = 3
  c = 7
  flood_fill(screen, r, c, screen[r][c], 3)

  print("After Flood-Fill:")
  for row in screen:
    print(row)
  print()
