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

.. math::

  logit(p) = log(p / 1 - p)

where p is the probability of the event occurring.

The logistic regression model is formulated as:

.. math::

  logit(p) = beta_0 + beta_1 * x_1 + beta_2 * x_2 + \dots + beta_k * x_k
