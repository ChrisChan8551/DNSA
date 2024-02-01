# https://leetcode.com/problems/climbing-stairs/?envType=study-plan-v2&envId=top-interview-150


# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


# Constraints:

# 1 <= n <= 45

def climbStairs(n):
    # Base cases: if n is 1, return 1; if n is 2, return 2
    if n == 1:
        return 1
    if n == 2:
        return 2

    # Initialize variables to store the number of ways for the last two steps
    prev_step, curr_step = 1, 2

    # Calculate the number of ways for each step from 3 to n
    for _ in range(3, n + 1):
        # Calculate the number of ways for the current step as the sum of the ways for the last two steps
        next_step = prev_step + curr_step

        # Update variables for the next iteration
        # prev_step, curr_step = curr_step, next_step
        prev_step = curr_step
        curr_step = next_step

    # Return the number of ways to climb to the top
    return curr_step


# print(climbStairs(2))  # 2
# print(climbStairs(3))  # 3
print(climbStairs(5))
# p = 1,2,3
# c = 2,3,3,3
