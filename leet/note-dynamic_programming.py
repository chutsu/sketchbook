"""
1. Visualize Examples
2. Find an appropriate subproblem
3. Find relationships amongst subproblem
4. Generalize the relationship
5. Implement by solving subproblems in order


Longest Increasing Subsequence (LIS)

  3 1 8 2 5


- All increasing subsequences are subsets of the original sequence
- All increasing subsequences have a start and end

LIS[k] = LIS ending at k



Common subproblems

- Ordered subsequence
- Random ordered subsequence
- Two lists of different sizes
- Single sublist
- Sub matrix


Common DP Problems:

- Fibonacci Numbers
- Zero One Knapsack
- Unbounded Knapsack
- Longest Common Subsequence
- Palindromes
- DFS + memoization (Longest Increasing Path in a Matrix, Path SUM III)
- Backtracking + memoization (Regex / Wildcard, Parition to K Equal Sum Subsets)
- State Machine (Best Time to Buy & Sell Stock)


## Multidimensional DP

Two dimensional DP problems are common, the following framework works
regardless of the number of dimensions:

- An indices along the input
- Explicit constraints given in the problem
- Variables the describes the status
- Datastructure to denote visited


# Bottom-Up (Tabulation)

Bottom-up is implemented with iteration and starts at the base cases.

  def fib(n):
    F = [0 for _ in range(n)]
    F[0] = 0
    F[1] = 1

    for i in range(2, n):
      F[i] = F[i - 1] + F[i - 2]

    return F[n]


# Top-Down (Memoization)

Top-down is implemented with recursion and made efficient with memoization.

A purely recursive method invokes unnecessary repeated computation. The solutio
is to memoize the results. Memoizing a results means to store the result of a
function call, usually in a hashmap or array, to cache the results and avoid
recalculating the result.

  memo = {}
  def fib(n):
    if i == 0 or i == 1:
      return n
    if n not in memo:
      memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]


## Which is better?

- Bottom up implementation's runtime is generally faster, due to its iterative
  properties over recursion.

- Top-Down implementation is generally easier to write. Ordering of the
  subproblems does not matter, but with tabulation it requires solving the
  problem in a logical ordering to solve the sub problems.


## Strategic Approach to Dynamic Programming

0. Identify the state. A state is a set of variables that can sufficiently
   describe a scenario.

1. A Function or data structure that will compute / contain the answer to the
   problem for every given state. Typically, top-down is implemented with a
   recursive function and hash-map. Bottom-up is implemented with nested for
   loops and an array.

2. A recurrance relation to transition between states. A recurrance relation is
   an equation that relates different states with each other.

3. Base cases. Finding the base cases is often the easiest part of solving a DP
   problem. Question to ask are "What state(s) can I find the answer to without
   using dynamic programming?"

"""
