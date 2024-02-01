# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.


# Example 1:

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false


# Constraints:

# 1 <= flowerbed.length <= 2 * 104
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length


def canPlaceFlowers(flowerbed, n):
    count = 0
    i = 0

    while i < len(flowerbed):
        if flowerbed[i] == 0:
            # Check if the current position and its neighbors are empty
            if (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1  # Plant a flower
                count += 1
        i += 1

    return count >= n

    # Iterate through the flowerbed and check for 0 and 1's.
    # if flowerbed is empty, check the left and right sides of the flowerbed to make sure it's empty.
    # assign flowerbed[i] 1 if plot is found
    # need to check first and last plot as edge cases
    # initialize a count of how many flowers can be planted.
    # if count is greater than n, then return true. Otherwise, return false


#! Example 1:
flowerbed = [1, 0, 0, 0, 1]
n = 1
# Output: true
print(canPlaceFlowers(flowerbed, n))

#! Example 2:
flowerbed = [1, 0, 0, 0, 1]
n = 2
# Output: false
print(canPlaceFlowers(flowerbed, n))

#! Example 3:
flowerbed = [1, 0, 0, 0, 0, 1]
n = 2
# Output: false
print(canPlaceFlowers(flowerbed, n))
