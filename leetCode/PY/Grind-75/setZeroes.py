# https://leetcode.com/problems/set-matrix-zeroes/
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

# Example 1:

# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# Example 2:


# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

# Constraints:

# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -231 <= matrix[i][j] <= 231 - 1


# Follow up:

# A straightforward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?

def setZeroes(matrix):
    # find position of zero
    # in order to prevent O(n^2) complexity, only loop through the values once to find the 0s.
    row = set()
    col = set()
    # loop through each row
    for r in range(len(matrix)):
        # loop through the column in each row
        for c in range(len(matrix[0])):
            if (matrix[r][c]) == 0:
                row.add(r)
                col.add(c)
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if (r in row or c in col):
                matrix[r][c] = 0



print(setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# print(setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
