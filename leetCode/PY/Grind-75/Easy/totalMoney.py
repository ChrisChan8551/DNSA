# https://leetcode.com/problems/calculate-money-in-leetcode-bank/

# Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

# He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
# Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.


#! Example 1:
# Input: n = 4
# Output: 10
# Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.

#! Example 2:
# Input: n = 10
# Output: 37
# Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.

#! Example 3:
# Input: n = 20
# Output: 96
# Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.


# Constraints:

# 1 <= n <= 1000

# Hint 1
# Simulate the process by keeping track of how much money Hercy is putting in and which day of the week it is, and use this information to deduce how much money John will put in the next day.

def totalMoney(n):
    # will need to create a loop to add up 7 days
    # for every new week will need to increase starting day by 1, declare a starting point. Initial starting point starts with 1
    start = 1
    total = 0
    while n > 0:
        for i in range(start, min(n, 8)):
            total += i
        start += 1
        n -= 7
    return total


def totalMoney(n):
    start = 1
    total = 0
    while n > 0:
        # Calculate the number of days in the current week
        days_in_week = min(n, 7)
        # Use the starting point in the range and correctly calculate the total
        for i in range(start, start + days_in_week):
            total += i
        # Increment the starting value for the next week
        start += 1
        # Decrease the number of days remaining by the number of days processed
        n -= days_in_week
    return total


#! Example 1:
n = 4
print(totalMoney(n))
# Output: 10
# Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.


#! Example 2:
n = 10
print(totalMoney(n))
# Output: 37
# Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.

#! Example 3:
# n = 20
# print(totalMoney(n))
# Output: 96
# Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.
