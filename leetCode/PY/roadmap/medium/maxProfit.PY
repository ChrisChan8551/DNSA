# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


#! Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

#! Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

#! brute force
# def maxProfit(prices):
#     # 2 pointer or sliding window
#     # declare variable to track maximum profit
#     # loop through the prices and compare right - left
#     # left, right = 0, len(prices)
#     n = len(prices)
#     max_profit = 0
#     for left in range(0, n):
#         for right in range(left + 1, n):
#             max_profit = max(max_profit, prices[right] - prices[left])
#             print(max_profit)
#     return max_profit

# def maxProfit(prices):
#     max_profit = 0
#     min_price = float('inf')
#     for i in range(len(prices)):
#         min_price = min(min_price, prices[i])
#         max_profit = max(max_profit, prices[i] - min_price)
#     return max_profit

#! better performance because it's more explicit reducing overhead using min and max methods above.
def maxProfit(prices):
    res = 0
    lowest = prices[0]
    for price in prices:
        if price < lowest:
            lowest = price
        current = price - lowest
        if current > res:
            res = current
    return res

    #! Example 1:
prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# #! Example 2:
# prices = [7, 6, 4, 3, 1]
# print(maxProfit(prices))
# # Output: 0
# # Explanation: In this case, no transactions are done and the max profit = 0.

#! Example 3:
prices = [5, 1, 5, 6, 7, 1, 10]
print(maxProfit(prices))
# Output: 9
# Explanation: In this case, no transactions are done and the max profit = 9.
