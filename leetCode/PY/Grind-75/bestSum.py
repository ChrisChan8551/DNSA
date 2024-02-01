
# #! brute force
# def bestSum(targetSum, numbers):
#     if targetSum == 0:
#         return []
#     if targetSum < 0:
#         return None
#     shortestCombination = None
#     for num in numbers:
#         remainder = targetSum - num
#         # this will return array or None.
#         remainderCombination = bestSum(remainder, numbers)
#         # if we enter this if statement, we can also generate the targetSum
#         if remainderCombination != None:
#             combination = [*remainderCombination, num]
#             # how to chose shortest combination / path?
#             # if combination is shorter than current shortest?
#             if shortestCombination == None or len(combination) < len(shortestCombination):
#                 #need to add shortestCombination == None because shortest combination is initialized is None. So that will never update.
#                 shortestCombination = combination

#     return shortestCombination


#! Memoization
def bestSum(targetSum, numbers, memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    shortestCombination = None
    for num in numbers:
        remainder = targetSum - num

        remainderCombination = bestSum(remainder, numbers, memo)

        if remainderCombination != None:
            combination = [*remainderCombination, num]

            if shortestCombination == None or len(combination) < len(shortestCombination):

                shortestCombination = combination

    memo[targetSum] = shortestCombination
    return shortestCombination


print(bestSum(7, [5, 3, 4, 7]))  # [7]
print(bestSum(8, [2, 3, 5]))  # [3,5]
print(bestSum(8, [1, 4, 5]))  # [4,4]
print(bestSum(100, [1, 2, 5, 25]))  # [25,25,25,25]
