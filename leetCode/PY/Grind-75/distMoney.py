# https://leetcode.com/problems/distribute-money-to-maximum-children/

# You are given an integer money denoting the amount of money (in dollars) that you have and another integer children denoting the number of children that you must distribute the money to.

# You have to distribute the money according to the following rules:

# All money must be distributed.
# Everyone must receive at least 1 dollar.
# Nobody receives 4 dollars.
# Return the maximum number of children who may receive exactly 8 dollars if you distribute the money according to the aforementioned rules. If there is no way to distribute the money, return -1.


# Example 1:

# Input: money = 20, children = 3
# Output: 1
# Explanation:
# The maximum number of children with 8 dollars will be 1. One of the ways to distribute the money is:
# - 8 dollars to the first child.
# - 9 dollars to the second child.
# - 3 dollars to the third child.
# It can be proven that no distribution exists such that number of children getting 8 dollars is greater than 1.
# Example 2:

# Input: money = 16, children = 2
# Output: 2
# Explanation: Each child can be given 8 dollars.


# Constraints:

# 1 <= money <= 200
# 2 <= children <= 30

# var distMoney = function (money, children) {
#     if (money < children) return -1;
#     if (money>children*8){
#         return children -1
#     }
#     let count = 0;
#     let amountLeft = money - children
#     let numberOf8 = Math.floor(amountLeft / 7)
#     let remainder = amountLeft % 7

#     if (remainder === 3 && numberOf8 > 0 && children - numberOf8 === 1) numberOf8--;

#     return numberOf8;
# };

def distMoney(money, children):
    if money < children:
        return -1
    if (children * 8 > money):
        return children - 1
    
    if money / children < 1:
        return -1

    if money == children:
        return 0
    if money <= 8:
        return 0

    amount = money - children
    print('amount: ', amount)

    numberOfeights = amount // 7
    print('numberOfeights: ', numberOfeights)
    remainder = amount % 7
    print('remainder: ', remainder)
    if (remainder == 3 and numberOfeights > 0 and (children - numberOfeights == 1)):
        return numberOfeights-1
    else:
        return numberOfeights

    # for i in range(money, 0, -1):
    #     money -= 8
    #     children -= 1


print(distMoney(17, 2))  # -> 1
# print(distMoney(20, 3))  # -> 1
# print(distMoney(16, 2))  # -> 2
