#!/usr/bin/env python3


def bubble_sort(array):
  N = len(array)
  for i in range(N):
    for j in range(0, N - i - 1):
      if array[j] > array[j + 1]:
        tmp = array[j]
        array[j] = array[j + 1]
        array[j + 1] = tmp


def selection_sort(array):
  N = len(array)
  for s in range(N):
    min_idx = s
    for i in range(s + 1, N):
      if array[i] < array[min_idx]:
        min_idx = i

    tmp = array[s]
    array[s] = array[min_idx]
    array[min_idx] = tmp


def insertion_sort(array):
  N = len(array)
  for i in range(1, N):
    a = array[i]
    j = i - 1

    while j >= 0 and a < array[j]:
      array[j + 1] = array[j]
      j -= 1

    array[j + 1] = a

  return array


if __name__ == "__main__":
  # Bubble sort
  a = [7, 2, 1, 6]
  bubble_sort(a)
  print(a)

  # Selection sort
  a = [7, 2, 1, 6]
  selection_sort(a)
  print(a)

  # Insertion sort
  a = [7, 2, 1, 6]
  insertion_sort(a)
  print(a)
