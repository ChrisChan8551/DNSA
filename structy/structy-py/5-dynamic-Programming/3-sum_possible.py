# Write a function sum_possible that takes in an amount and a list of positive numbers. The function should return a boolean indicating whether or not it is possible to create the amount by summing numbers of the list. You may reuse numbers of the list as many times as necessary.

# You may assume that the target amount is non-negative.

#! brute force (O m^n)
# def sum_possible(amount, numbers):
#     # base cases
#     if (amount == 0):
#         return True
#     if (amount < 0):
#         return False
#     for num in numbers:
#         remainder = amount - num
#         if sum_possible(remainder, numbers) == True:
#             return True
#     return False

#! with memoization
# when you decide for a key into memo object. Notice which arguments will impact the return value which is AMOUNT
def sum_possible(amount, numbers, memo={}):
    # base cases
    if amount in memo:
        return memo[amount]
    if (amount == 0):
        return True
    if (amount < 0):
        return False
    for num in numbers:
        remainder = amount - num
        if sum_possible(remainder, numbers, memo) == True:
            memo[amount] = True
            return True
    memo[amount] = False
    return False

# #! TEST_00
# print(sum_possible(8, [5, 12, 4]))  # -> True, 4 + 4

# #! TEST_01
# print(sum_possible(15, [6, 2, 10, 19]))  # -> False

# #! TEST_02
# print(sum_possible(13, [6, 2, 1]))  # -> True

# #! TEST_03
# print(sum_possible(103, [6, 20, 1]))  # -> True

# #! TEST_04
# print(sum_possible(12, []))  # -> False

# #! TEST_05
# print(sum_possible(12, [12]))  # -> True

# #! TEST_06
# print(sum_possible(0, []))  # -> True


# #! TEST_07
print(sum_possible(271, [10, 8, 265, 24]))  # -> False

# #! TEST_08
print(sum_possible(2017, [4, 2, 10]))  # -> False

# #! TEST_09
# print(sum_possible(13, [3, 5]))  # -> true

# #! TEST_10
# print(sum_possible(10, [4, 5, 7]))  # -> true
