import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[1, 2], [4, 5], [7, 8]])

res = np.zeros((3, 2))

for i in range(A.shape[0]):
  for j in range(A.shape[1]):
    if A[i, j] == 0.0:
      continue

    for k in range(B.shape[1]):
      res[i, k] += A[i, j] * B[j, k]

print(res)
print(A @ B)
