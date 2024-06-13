#!/usr/bin/env python3
"""
LeetCode 121: Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on
the ith day.

You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot
achieve any profit, return 0.
"""

if __name__ == "__main__":
  prices = [7, 1, 5, 3, 6, 4]

  left = 0
  right = 0
  max_profit = 0

  while right < len(prices):
    profit = prices[right] - prices[left]
    if profit > 0:
      max_profit = max(profit, max_profit)
    else:
      left = right

    right += 1

  print(max_profit)
