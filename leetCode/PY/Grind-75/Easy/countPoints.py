# https://leetcode.com/problems/rings-and-rods/

# There are n rings and each ring is either red, green, or blue. The rings are distributed across ten rods labeled from 0 to 9.

# You are given a string rings of length 2n that describes the n rings that are placed onto the rods. Every two characters in rings forms a color-position pair that is used to describe each ring where:

# The first character of the ith pair denotes the ith ring's color ('R', 'G', 'B').
# The second character of the ith pair denotes the rod that the ith ring is placed on ('0' to '9').
# For example, "R3G2B1" describes n == 3 rings: a red ring placed onto the rod labeled 3, a green ring placed onto the rod labeled 2, and a blue ring placed onto the rod labeled 1.

# Return the number of rods that have all three colors of rings on them.


#! Example 1:
# Input: rings = "B0B6G0R6R0R6G9"
# Output: 1
# Explanation:
# - The rod labeled 0 holds 3 rings with all colors: red, green, and blue.
# - The rod labeled 6 holds 3 rings, but it only has red and blue.
# - The rod labeled 9 holds only a green ring.
# Thus, the number of rods with all three colors is 1.

#! Example 2:
# Input: rings = "B0R0G0R9R0B0G0"
# Output: 1
# Explanation:
# - The rod labeled 0 holds 6 rings with all colors: red, green, and blue.
# - The rod labeled 9 holds only a red ring.
# Thus, the number of rods with all three colors is 1.

#! Example 3:
# Input: rings = "G4"
# Output: 0
# Explanation:
# Only one ring is given. Thus, no rods have all three colors.


# Constraints:
# rings.length == 2 * n
# 1 <= n <= 100
# rings[i] where i is even is either 'R', 'G', or 'B' (0-indexed).
# rings[i] where i is odd is a digit from '0' to '9' (0-indexed).

#! Hint 1
# For every rod, look through ‘rings’ to see if the rod contains all colors.
#! Hint 2
# Create 3 booleans, 1 for each color, to store if that color is present for the current rod. If all 3 are true after looking through the string, then the rod contains all the colors.


# def countPoints(rings):
#     # will need count variable
#     # loop through the rings string
#     # first char should be a letter, and second should be a number
#     # declare empty array for to keep track of rods
#     # need to preallocate [] for rods otherwise will get out of index error
#     rods = [[] for _ in range(10)]
#     count = 0
#     n = len(rings)
#     for i in range(0, n, 2):
#         color = rings[i]
#         rod = int(rings[i+1])
#         rods[rod].append(color)

#     for rod in rods:
#         if 'R' in rod and 'G' in rod and 'B' in rod:
#             count += 1
#     return count

#! alternative short solution
def countPoints(rings):
    count = 0
    for i in range(10):
        i = str(i)
        if 'R' + i in rings and 'G' + i in rings and 'B' + i in rings:
            count += 1
    return count


#! Example 1:
rings = "B0B6G0R6R0R6G9"
print(countPoints(rings))
# Output: 1
# Explanation:
# - The rod labeled 0 holds 3 rings with all colors: red, green, and blue.
# - The rod labeled 6 holds 3 rings, but it only has red and blue.
# - The rod labeled 9 holds only a green ring.
# Thus, the number of rods with all three colors is 1.

#! Example 2:
rings = "B0R0G0R9R0B0G0"
print(countPoints(rings))
# Output: 1
# Explanation:
# - The rod labeled 0 holds 6 rings with all colors: red, green, and blue.
# - The rod labeled 9 holds only a red ring.
# Thus, the number of rods with all three colors is 1.

#! Example 3:
rings = "G4"
print(countPoints(rings))
# Output: 0
# Explanation:
# Only one ring is given. Thus, no rods have all three colors.