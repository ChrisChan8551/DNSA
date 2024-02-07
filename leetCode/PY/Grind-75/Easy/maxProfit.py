# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.


# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

#! O(n) with 1 loop
def maxProfit(prices):
    #need a variable to track for min price and max profit.
    minPrice = float('inf')
    maxProfit = 0
    #loop through all the prices sequentially
    for price in prices:
        minPrice = min(minPrice, price)

        #max number needs to be greater index than min price.
        #max profit = max - min
        maxProfit = max(maxProfit, price - minPrice)
    return maxProfit


# #! O(n) with 2 pointer method
# def maxProfit(prices):
#     if not prices or len(prices) == 1:
#         return 0

#     left = 0  # Pointer for buying day
#     right = 1  # Pointer for selling day
#     max_profit = 0

#     while right < len(prices):
#         if prices[right] > prices[left]:
#             # Update the maximum profit if a higher profit is found
#             max_profit = max(max_profit, prices[right] - prices[left])
#         else:
#             # Update the buying day if a lower price is encountered
#             left = right

#         # Move the selling day pointer to the next day
#         right += 1

#     return max_profit


print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([7, 6, 4, 3, 1]))
print(maxProfit([2, 1]))
print(maxProfit([2, 1, 2, 0, 1]))
