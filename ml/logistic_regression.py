#!/usr/bin/env python3
"""
Logistic Regression
===================

Logistic regression is a statistical method used for modeling the probability
of a **binary outcome** (i.e., a dependent variable with two possible outcomes,
such as success/failure, yes/no, or 0/1) based on one or more predictor
variables (independent variables). It is a type of regression analysis used
when the dependent variable is categorical.

The core of logistic regression is the logit function, which is the natural
logarithm of the odds of the dependent event occurring.

The logit function is expressed as:

  logit(p) = log(p / 1 - p)

where p is the probability of the event occurring.

The logistic regression model is formulated as:

  logit(p) = beta_0 + beta_1 * x_1 + beta_2 * x_2 + \dots + beta_k * x_k

"""
import numpy as np
from numpy import exp
from numpy import log
import matplotlib.pylab as plt

# Step 1: Generate Synthetic Data
np.random.seed(0)
N = 50  # Sample size

# Class 0
x0 = np.random.normal(2, 1, N)
y0 = np.random.normal(2, 1, N)

# Class 1
x1 = np.random.normal(4, 1, N)
y1 = np.random.normal(4, 1, N)

# Combine into a single dataset
X = np.vstack((np.hstack((x0, x1)), np.hstack((y0, y1)))).T
Y = np.hstack((np.zeros(N), np.ones(N)))

# Add a column of ones to X to account for the bias term (intercept)
X = np.hstack((np.ones((X.shape[0], 1)), X))


# Step 2: Implement Logistic Regression
def sigmoid(z):
  return 1 / (1 + exp(-z))


def cost_function(X, Y, theta):
  m = len(Y)
  h = sigmoid(X @ theta)
  epsilon = 1e-5
  cost = (-1 / m) * (Y @ log(h + epsilon) + (1 - Y) @ log(1 - h + epsilon))
  return cost


def gradient_descent(X, Y, theta, gamma, num_iter):
  m = len(Y)
  cost_history = []

  for i in range(num_iter):
    h = sigmoid(X @ theta)
    theta -= (gamma / m) * X.T @ (h - Y)
    cost = cost_function(X, Y, theta)
    cost_history.append(cost)

  return theta, cost_history


# Initialize parameters
theta = np.zeros(X.shape[1])
gamma = 0.1
num_iter = 1000

# Train the model
theta, cost_history = gradient_descent(X, Y, theta, gamma, num_iter)

# Step 3: Plot the Decision Boundary
plt.figure(figsize=(10, 6))

# Plot the data points
plt.scatter(x0, y0, color='red', label='Class 0')
plt.scatter(x1, y1, color='blue', label='Class 1')

# Plot the decision boundary
x_values = [np.min(X[:, 1]), np.max(X[:, 1])]
y_values = -(theta[0] + np.dot(theta[1], x_values)) / theta[2]
plt.plot(x_values, y_values, label='Decision Boundary')

# Add labels and legend
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.title('Logistic Regression Decision Boundary')

# Show the plot
plt.show()
