#!/usr/bin/env python3
import numpy as np


A = np.array([[1.0, 0.0, 0.0], [-1.0, 0.0, 3.0]])
B = np.array([[7.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])

A = np.random.rand(3, 10)
B = np.random.rand(10, 2)

# print(A)
# print(B)
print(A @ B)

Am, An = A.shape
Bm, Bn = B.shape
Cm, Cn = Am, Bn

C = np.zeros((Am, Bn))
for i in range(Am):
  for j in range(An):
    for k in range(Bn):
      C[i, k] += A[i, j] * B[j, k]

print(C)
