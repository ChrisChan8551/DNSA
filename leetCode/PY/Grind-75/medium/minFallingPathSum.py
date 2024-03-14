# https://leetcode.com/problems/minimum-falling-path-sum/

# Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

# A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

#! Example 1:
# Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
# Output: 13
# Explanation: There are two falling paths with a minimum sum as shown.

#! Example 2:
# Input: matrix = [[-19,57],[-40,-5]]
# Output: -59
# Explanation: The falling path with a minimum sum is shown.


# Constraints:

# n == matrix.length == matrix[i].length
# 1 <= n <= 100
# -100 <= matrix[i][j] <= 100

#! dynamic programming problem

def minFallingPathSum(matrix, memo={}):
    # DFS to check each different path
    # select the lowest number on the first row
    # need to DFS for each starting point on row 0
    # need to check for inbounds, only col can go out of bounds due to base case.

    N = len(matrix)

    def _inbounds(c):
        return 0 <= c < N

    def _dp(r, c):
        # need 2 base cases (success and fail)

        # success
        if r == N:
            return 0
        # fail
        if not _inbounds(c):
            return float('inf')

        # memo base case
        if (r, c) in memo:
            return memo[(r, c)]

        left = _dp(r + 1, c - 1)
        mid = _dp(r + 1, c)
        right = _dp(r + 1, c + 1)

        memo[(r, c)] = min(left, mid, right) + matrix[r][c]
        return memo[(r, c)]

    min_sum = float('inf')
    memo = {}
    for c in range(N):
        min_sum = min(min_sum, _dp(0, c))

    return min_sum


#! Example 1:
matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
print(minFallingPathSum(matrix))
# Output: 13
# Explanation: There are two falling paths with a minimum sum as shown.

#! Example 2:
matrix = [[-19, 57], [-40, -5]]
print(minFallingPathSum(matrix))
# Output: -59
# Explanation: The falling path with a minimum sum is shown.
