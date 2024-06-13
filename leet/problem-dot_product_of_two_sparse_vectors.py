#!/usr/bin/env python3
"""
LeetCode 1570: Dot product of two sparse vectors

Given two sparse vectors, compute their dot product.

Implement class SparseVector:

    SparseVector(nums) Initializes the object with the vector nums
    dotProduct(vec) Compute the dot product between the instance of SparseVector and vec

A sparse vector is a vector that has mostly zero values, you should store the
sparse vector efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?
"""


class SparseVector:
  def __init__(self, nums):
    self.data = {}
    for i, val in enumerate(nums):
      self.data[i] = val

  def dotProduct(self, vec):
    s = 0

    if len(self.data) < len(vec.data):
      for i, val in self.data.items():
        if i in vec.data:
          s += vec.data[i] * self.data[i]

    else:
      for i, val in vec.data.items():
        if i in self.data:
          s += vec.data[i] * self.data[i]

    return s


if __name__ == "__main__":
  nums1 = [1, 0, 0, 2, 3]
  nums2 = [0, 3, 0, 4, 0]
  v1 = SparseVector(nums1)
  v2 = SparseVector(nums2)
  assert v1.dotProduct(v2) == 8
