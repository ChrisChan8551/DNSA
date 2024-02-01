# Write a function fib that takes in a number argument, n, and returns the n-th number of the Fibonacci sequence.

# The 0-th number of the sequence is 0.

# The 1-st number of the sequence is 1.

# To generate further numbers of the sequence, calculate the sum of previous two numbers.

# Solve this recursively.

# def fib(n, memo={}):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     elif n in memo:
#         return memo[n]
#     else:
#         result = fib(n - 1, memo) + fib(n - 2, memo)
#         memo[n] = result
#         return result

# def fib(n):
#     # Base cases: 0-th number is 0, and 1-st number is 1
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         # Calculate Fibonacci numbers for n >= 2
#         a, b = 0, 1
#         for _ in range(2, n + 1):
#             a, b = b, a + b
#         return b

#! memoization
def fib(n, memo={}):
    if (n in memo):# base case
        return memo[n]

    if (n <= 2):
        return 1
    memo[n] = fib(n-1, memo) + fib(n-2, memo) # saving the return value as memo[n]
    return memo[n]

#! TEST_00
print(fib(0))  # -> 0

#! TEST_01
print(fib(1))  # -> 1

#! TEST_02
print(fib(2))  # -> 1

#! TEST_03
print(fib(3))  # -> 2

#! TEST_04
print(fib(4))  # -> 3

#! TEST_05
print(fib(5))  # -> 5

#! TEST_06
print(fib(35))  # -> 9227465

#! TEST_07
print(fib(46))  # -> 1836311903

print(fib(80))  # -> 23416728348467685
