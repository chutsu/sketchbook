Linear Discriminant Analysis (LDA)
==================================

Linear discriminant analysis is a classifier with a linear decision boundary,
it does so by fitting class conditional densities to the data using Bayes'
rule. Assumes:

- Each class a Gaussian density
- All classes share the same covariance matrix :math:`\Sigma`

.. math::

  p(y = k | x)
    &= \dfrac{p(x | y = k) \; p(y = k)}{p(x)} \\\\
    &= \dfrac{ p(x | y = k) \; p(y = k)}
        {\sum_{l} p(x | y = l) p(y = l)}

.. math::

  p(x | y = k) =
    \dfrac{1}{(2 \pi)^{d/2} \; \left| \Sigma \right|^{\frac{1}{2}}}
    \enspace
    \exp
    \left(
      -\dfrac{1}{2}
      (x - \mu_{k})^{T}
      \Sigma^{-1}_{k}
      (x - \mu_{k})
    \right)

.. math::

  \log \left( p(y = k | x) \right)
  &=
  \log \left( \dfrac{p(x | y = k) \; p(y = k)}{p(x)} \right)
  \\\\
  &=
  \log \left( p(x | y = k) \right)
  + \log \left( p(y = k) \right)
  - \log \left( p(x) \right)
