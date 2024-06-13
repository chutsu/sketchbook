#!/usr/bin/env python3


def merge_intervals(intervals):
  intervals = sorted(intervals, key=lambda x: x[0])
  results = []

  for start, end in intervals:
    if len(results) == 0 or results[-1][1] < start:
      results.append([start, end])

    else:
      results[-1][1] = max(results[-1][1], end)

  return results


x = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(x))
