#!/usr/bin/env python3
"""
LeetCode 528: Random Pick with Weight
-------------------------------------
You are given a 0-indexed array of positive integers w where w[i] describes the
weight of the ith index.

You need to implement the function pickIndex(), which randomly picks an index
in the range [0, w.length - 1] (inclusive) and returns it. The probability of
picking an index i is w[i] / sum(w).

For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) =
0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75
(i.e., 75%).
"""
import random
import matplotlib.pylab as plt


def weighted_random(weights):
  # Form prefix sums
  prefix_sums = []
  s = 0
  for w in weights:
    s += w
    prefix_sums.append(s)

  # Random sample weighted distribution
  target = s * random.random()
  for i, prefix_sum in enumerate(prefix_sums):
    if prefix_sum > target:
      return i


if __name__ == "__main__":
  weights = [4, 6]
  n = 10000

  data = []
  for i in range(n):
    data.append(weighted_random(weights))

  plt.hist(data)
  plt.show()
