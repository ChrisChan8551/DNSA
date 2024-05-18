# https://leetcode.com/problems/determine-color-of-a-chessboard-square/

# You are given coordinates, a string that represents the coordinates of a square of the chessboard. Below is a chessboard for your reference.


# Return true if the square is white, and false if the square is black.

# The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first, and the number second.


#! Example 1:
# Input: coordinates = "a1"
# Output: false
# Explanation: From the chessboard above, the square with coordinates "a1" is black, so return false.

#! Example 2:
# Input: coordinates = "h3"
# Output: true
# Explanation: From the chessboard above, the square with coordinates "h3" is white, so return true.

#! Example 3:
# Input: coordinates = "c7"
# Output: false


# Constraints:

# coordinates.length == 2
# 'a' <= coordinates[0] <= 'h'
# '1' <= coordinates[1] <= '8'
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 80.1K
# Submissions
# 102.3K
# Acceptance Rate
# 78.3%
# Topics
# Companies
# Hint 1
# Convert the coordinates to (x, y) - that is, "a1" is (1, 1), "d7" is (4, 7).
# Hint 2
# Try add the numbers together and look for a pattern.


def squareIsWhite(coordinates):
    pass


#! Example 1:
coordinates = "a1"
print(squareIsWhite(coordinates))
# Output: false
# Explanation: From the chessboard above, the square with coordinates "a1" is black, so return false.

#! Example 2:
coordinates = "h3"
print(squareIsWhite(coordinates))
# Output: true
# Explanation: From the chessboard above, the square with coordinates "h3" is white, so return true.

#! Example 3:
coordinates = "c7"
print(squareIsWhite(coordinates))
# Output: false
