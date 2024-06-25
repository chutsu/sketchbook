Bayes Classifier
================

Recall the Bayes' Theorem:

.. math::
  :label: bayes_classifier

  P(Y = k | X = x)
    &= \dfrac{P(X | Y = k) \; P(Y = k)}{P(X = x)} \\
    &= \dfrac{P(X | Y = k) \; P(Y = k)}
        {\sum_{i}^{K} P(X | Y = i) P(Y = i)} \\
    &= \dfrac{f_k(x) \; \pi_k}
        {\sum_{i}^{K} f_i(x) \; \pi_i}



where the left hand side, :math:`P(Y = k | X = x)`, is called the posterior
probability and gives the probability that an observation :math:`X = x` belongs
to the :math:`k^{\text{th}}` class. Let :math:`f_k(X) \equiv P(X | Y = k)` denote
the density function of :math:`X` for an observation that comes from the
:math:`k^{\text{th}}` class, and :math:`\pi_k \equiv P(Y = k)` represent the
prior probability that a randomly chosen observation comes from the
:math:`k^{\text{th}}` class.

Rather than attempting to compute the posterior probability :math:`P(Y = k | X
= x)`, we can plug in estimates of :math:`f_k(x)` and :math:`\pi_k`. The
challenge is estimating the density function :math:`f_k(x)`. Different
classifiers use different estimates of :math:`f_k(x)` to approximate the Bayes
classifier.


Linear Discriminant Analysis (LDA)
----------------------------------

Linear Discriminant Analysis (LDA) is a classifier with a linear decision
boundary, it does so by fitting class conditional densities to the data using
Bayes' rule.

LDA assumes:

- Each class is Gaussian with a mean :math:`\mu_k`, and variance
  :math:`\sigma^{2}_{k}` for the :math:`k^{\text{th}}` class

.. math::
  :label: normal_dist

  f_k(x) = \dfrac{1}{\sqrt{2\pi} \; \sigma_k}
    \exp \left( -\dfrac{1}{2\sigma^{2}_{k}} (x - \mu_k)^{2} \right)


- All classes share the variance

.. math::
  :label: equal_var

  \sigma^{2}_{1} = \sigma^{2}_{2} = \cdots = \sigma^{2}_{K}



Linear Discriminant Analysis for :math:`p = 1`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Assume we have only one predictor, :math:`p = 1`. Substituting the normal
density function :eq:`normal_dist` and shared variance :eq:`equal_var`
into the Bayes classifier :eq:`bayes_classifier`, we get:

.. math::

  P(Y = k | X = x)
    &= \dfrac{f_k(x) \; \pi_k}
        {\sum_{i}^{K} f_i(x) \; \pi_i}
    \\
    &= \dfrac{
      \pi_k \;
      \frac{1}{\sqrt{2\pi} \; \sigma}
        \exp \left( -\frac{1}{2\sigma^{2}} (x - \mu_k)^{2} \right)
    }
    {
      \sum_{i}^{K}
      \pi_i \;
      \frac{1}{\sqrt{2\pi} \; \sigma}
        \exp \left( -\frac{1}{2\sigma^{2}} (x - \mu_i)^{2} \right)
    }

taking the log on both sides and rearranging the terms,

.. math::

  \log P(Y = k | X = x)
    &=
      \log ( \pi_k )
      - \log ( \sqrt{2\pi} \; \sigma )
      -\frac{1}{2\sigma^{2}} (x - \mu_k)^{2}
      + \text{const} \\
    &=
      \log ( \pi_k )
      -\frac{1}{2\sigma^{2}} (x - \mu_k)^{2}
      + \text{const} \\
    &=
      \log ( \pi_k )
      -\frac{x^2}{{2\sigma^{2}}}
      -\frac{2 x \mu_k}{{2\sigma^{2}}}
      +\frac{\mu_k^2}{{2\sigma^{2}}}
      + \text{const} \\
    &=
      \log ( \pi_k )
      -\frac{x \mu_k}{{\sigma^{2}}}
      +\frac{\mu_k^2}{{2\sigma^{2}}}
      + \text{const} \\

we arrive at the Linear discriminant function :math:`\delta_k(x)`

.. math::
  :label: ldf

  \delta_k(x) =
    \log ( \pi_k )
    -\frac{x \mu_k}{{\sigma^{2}}}
    +\frac{\mu_k^2}{{2\sigma^{2}}}

The Bayes decision boundary is the point for which :math:`\delta_1(x) = \delta_2(x)`:

.. math::

  x = \dfrac{\mu^{2}_{1} - \mu^{2}_{2}}{2 (\mu_{1} - \mu_{2})}
    = \dfrac{\mu_{1} + \mu_{2}}{2}


The Linear Discriminant analysis (LDA) method approximates the Bayes classifier
by plugging in estimates for :math:`\pi_k`, :math:`\mu_k` and
:math:`\sigma^{2}` into the Linear discriminant function in :eq:`ldf`.

.. math::

  \hat{\mu}_k &= \dfrac{1}{n_k} \sum_{i:y_i = k} x_i \\
  \hat{\sigma}^{2} &= \dfrac{1}{n - K}
    \sum_{k=1}^{K} \sum_{i:y_i=k} (\mu_i - \hat{\mu}_k)^2

where :math:`n` is the total number of observations, :math:`n_k` is the number
of observations in the :math:`k^{\text{th}}` class. The estimate for
:math:`\mu_k` and :math:`\hat{\sigma}^{2}` are simply the mean and variance of
all observations of the :math:`k^{\text{th}}` class.


Linear Discriminant Analysis for :math:`p > 1`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the multiple predictor case, we assume that observations :math:`\mathbf{X} =
(\mathbf{X}_1, \mathbf{X}_2, \cdots, \mathbf{X}_p)` is drawn from multi-variate
Gaussian distribution, with a class-specific mean vector and common covariance
matrix. Formally, the multivariate Gaussian density is defined as:

.. math::

  f(x) = \dfrac{1}{(2\pi)^{\frac{p}{2}} \; \|\Sigma_k\|^{\frac{1}{2}}}
    \exp
    \left(
      - \frac{1}{2}
      (x - \mu)^{T}
      \Sigma^{-1}
      (x - \mu)
    \right)

In the case of :math:`p > 1` predictors, the Linear discriminant function is:

.. math::
  :label: ldf_multi

  \delta_k(x) =
    \log ( \pi_k )
    + \mathbf{x}^{T} \boldsymbol{\Sigma^{-1}} \mathbf{\mu}_k
    + \dfrac{1}{2} \mathbf{\mu}_{k}^{T} \boldsymbol{\Sigma^{-1}} \mathbf{\mu}_{k}

this is the matrix / vector version of :eq:`ldf`.



Quadratic Discriminant Analysis (QDA)
-------------------------------------

Linear Discriminant Analysis (LDA) in assumes observations are drawn from a
multivariate Gaussian distribution with a class-specific mean and a *common*
covariance matrix to all :math:`K` classes.

Quadratic Discriminant Analysis (QDA) is an alternative that assumes each class
has its own covariance matrix. With this, the Bayes classifier assigns an
observation :math:`X = x` to the class for which the Quadratic Discriminant
function is the largest

.. math::
  :label: qda

  \delta_k(x)
    =
      -\dfrac{1}{2}
        (\mathbf{x} - \boldsymbol{\mu}_k)^{T}
        \boldsymbol{\Sigma}_k
        (\mathbf{x} - \boldsymbol{\mu}_k)
      -\dfrac{1}{2} \log \| \boldsymbol{\Sigma}_k \|
      +\log \pi_k

Unlike the Linear discriminant function in :eq:`ldf_multi`, the quantity
:math:`x` is quadratic in the function :eq:`qda`. This is why this approach is
called the Quadratic Discriminant Analysis.

The choice between using LDA or QDA is essentially the bias-variance trade-off.
LDA is less flexible than QDA, so has lower variance and potentially lead to
improved prediction performance. However, if the assumption that :math:`K`
classes share a common covariance matrix is incorrect, then LDA would suffer
from a high bias. In contrast QDA is often the go to if training set is very
large, so that the variance of the classifier is not a major concern, or if the
common covariance matrix fo :math:`K` classes is clearly incorrect.



Naive Bayes
-----------

Bayes theorem in :eq:`bayes_classifier` provides an expresion for the
posterior probability :math:`P(Y = k | X = x)`, to use it we need estimates for
the priors, :math:`\pi_1, \cdots, \pi_K`, and measurement densities,
:math:`f_1(x), \cdots, f_K(x)`. While estimating the priors is straighforward,
estimating the measurement densities is more challenging. In LDA and QDA, both
approaches made strong assumptions that :math:`f_k` is a multivariate gaussian
normal density function, with a class specific mean :math:`\boldsymbol{\mu}_k`,
and covariance matrix :math:`\boldsymbol{\Sigma}` (shared covariance in the
case of LDA, and different covariances with QDA).

The naive Bayes classifier takes a different approach for estimating the
measurement densities :math:`f_1(x), \cdots, f_K(x)`. Instead of assuming these
functions belong to a particular family of distributions (e.g. multivariate
normal), we instead make a single assumption:

  Within the :math:`k^{\text{th}}` class, the :math:`p` predictors are
  independent

or stated mathematically:

.. math::
  :label: naive_bayes_assumption

  f_k(x) = f_{k1}(x_1) \times f_{k2}(x_2) \times \cdots \times f_{kp}(x_p)

where :math:`f_{kj}` is the density function of the :math:`j^{\text{th}}`
predictor among observations in the :math:`k^{\text{th}}` class.

This is powerful because this effectively means we make no assumptions about
the associations between each predictor, each predictor is independent within
its class. In practice, there will be associations between predictors, this
assumption is made for convenience and it often leads to decent results,
especially in scenarios where the number of sample data :math:`n` is not large
enough.

Plugging the naive Bayes assumption :eq:`naive_bayes_assumption` into Bayes
theorem :eq:`bayes_classifier`,

.. math::
  P(Y = k | X = x) =
    \dfrac{
      \pi_k
      \times
      f_{k1}(x_1) \times f_{k2}(x_2) \times \cdots \times f_{kp}(x_p)
    }
    {
      \sum_{i = 1}^{K}
      \pi_i
      \times
      f_{i1}(x_1) \times f_{i2}(x_2) \times \cdots \times f_{ip}(x_p)
    }

for :math:`k = 1, \cdots, K`.



References
^^^^^^^^^^

:cite:empty:`James2023:SpringerNature`

.. bibliography::


