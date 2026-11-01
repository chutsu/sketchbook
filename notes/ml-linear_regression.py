#!/usr/bin/env python3
import numpy as np
from numpy.linalg import inv
import matplotlib.pylab as plt


if __name__ == "__main__":
  # Generate synthetic data
  np.random.seed(42)
  N = 100  # Number of samples
  beta0_gnd = 4.0
  beta1_gnd = 3.0
  X = 2 * np.random.rand(N, 1)
  Y = beta0_gnd + beta1_gnd * X + np.random.randn(N, 1)

  # Perform linear regression
  A = np.block([np.ones((100, 1)), X])
  theta = inv(A.T @ A) @ A.T @ Y
  intercept = theta[0][0]
  slope = theta[1][0]

  # Plot results
  plt.plot(X, Y, "k.", label="Sample Data")
  plt.plot(X, A.dot(theta), color='red', linewidth=2, label='Estimate')
  plt.plot(X, A.dot(np.array([beta0_gnd, beta1_gnd])), color='k', linewidth=2, label='Ground Truth')
  plt.xlabel("x")
  plt.ylabel("y")
  plt.legend(loc=0)
  plt.show()
