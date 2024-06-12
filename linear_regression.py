#!/usr/bin/env python3
"""
Linear Regression
=================

In linear regression we typically have a linear model of the form:

..math:

  y \approx beta0 + beta1 * x

where the goal is to estimate beta0 and beta1 using pairs of data (x, y).
The most common approach to estimating the coefficients involves minimizing the
least squares criterion.

Residual Sum of Squares (RSS):

..math:

  \begin{align}
    RSS &= e_1^2 + e_2^2 + e_3^2 + \dots + e_n^2 \\
         = \Sum_{i = 1}^{n} (y_i - \hat{y}_{i})^{2}
  \begin{end}


Standard Error:

  VAR(\hat{\mu}) = SE(\hat{\mu})^{2} = \dfrac{\sigma^{2}}{n}

where :math`\sigma` is the standard deviation of each of the realizations of
:math`y_i`. The standard error tells us the average amount the estimate has
deviated from the actual.

A confidence interval (CI) is a range of values, derived from sample
statistics, that is likely to contain the value of an unknown population
parameter. The confidence interval gives an estimated range of values which is
likely to include the parameter being estimated, expressed at a given level of
confidence.

For a population mean, the confidence interval can be calculated as:

..math:

  CI = \bar{x} \pm z(\dfrac{\sigma}{n})

"""
import numpy as np
import matplotlib.pylab as plt

# Generate synthetic data
np.random.seed(42)
N = 100  # Number of samples
beta0_gnd = 4.0
beta1_gnd = 3.0
X = 2 * np.random.rand(N, 1)
Y = beta0_gnd + beta1_gnd * X + np.random.randn(N, 1)

# Perform linear regression
A = np.c_[np.ones((100, 1)), X]
theta = np.linalg.inv(A.T @ A) @ A.T @ Y
intercept = theta[0][0]
slope = theta[1][0]

# Plot results
plt.plot(X, Y, "k.", label="Sample Data")
plt.plot(X, A.dot(theta), color='red', linewidth=2, label='Estimate')
plt.plot(X, A.dot(np.array([beta0_gnd, beta1_gnd])), color='k', linewidth=2, label='Ground Truth')
plt.legend(loc=0)
plt.show()
