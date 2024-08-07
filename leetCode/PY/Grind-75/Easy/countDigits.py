# https://leetcode.com/problems/count-the-digits-that-divide-a-number/

# Given an integer num, return the number of digits in num that divide num.

# An integer val divides nums if nums % val == 0.


#! Example 1:
# Input: num = 7
# Output: 1
# Explanation: 7 divides itself, hence the answer is 1.

#! Example 2:
# Input: num = 121
# Output: 2
# Explanation: 121 is divisible by 1, but not 2. Since 1 occurs twice as a digit, we return 2.

#! Example 3:
# Input: num = 1248
# Output: 4
# Explanation: 1248 is divisible by all of its digits, hence the answer is 4.


# Constraints:

# 1 <= num <= 109
# num does not contain 0 as one of its digits.

def countDigits(num):
    count = 0
    word = str(num)
    for char in word:
        if num % int(char) == 0:
            count += 1
    return count


#! Example 1:
num = 7
print(countDigits(num))
# Output: 1
# Explanation: 7 divides itself, hence the answer is 1.

#! Example 2:
num = 121
print(countDigits(num))
# Output: 2
# Explanation: 121 is divisible by 1, but not 2. Since 1 occurs twice as a digit, we return 2.

#! Example 3:
num = 1248
print(countDigits(num))
# Output: 4
# Explanation: 1248 is divisible by all of its digits, hence the answer is 4.
