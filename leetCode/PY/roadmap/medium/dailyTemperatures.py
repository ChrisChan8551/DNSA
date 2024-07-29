# https://leetcode.com/problems/daily-temperatures/

# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.


#! Example 1:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

#! Example 2:
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]

#! Example 3:
# Input: temperatures = [30,60,90]
# Output: [1,1,0]


# Constraints:

# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100

#! Hint 1
# If the temperature is say, 70 today, then in the future a warmer temperature must be either 71, 72, 73, ..., 99, or 100. We could remember when all of them occur next.

def dailyTemperatures(temperatures):
    n = len(temperatures)
    # the length of the result can only be as long as temperatures array. Because of that, you need to pre-allocate the result array with 0's x length.
    result = [0] * n
    # use a stack to keep track of indices of temperatures
    stack = []
    #loop through the temperatures array
    for i in range(n):
        # if there's something in the stack, check if the top of the stack is current temperature is lower than the top of the stack (stack[-1])
        while stack and temperatures[stack[-1]] < temperatures[i]:
            index = stack.pop()
            result[index] = i - index
        # add index to the stack if current temperature is higher.
        stack.append(i)
    return result


#! Example 1:
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# stack = [73
    #
    # ]
print(dailyTemperatures(temperatures))
# Output: [1,1,4,2,1,1,0,0]

#! Example 2:
temperatures = [30, 40, 50, 60]
print(dailyTemperatures(temperatures))
# Output: [1,1,1,0]

#! Example 3:
temperatures = [30, 60, 90]
print(dailyTemperatures(temperatures))
# Output: [1,1,0]
