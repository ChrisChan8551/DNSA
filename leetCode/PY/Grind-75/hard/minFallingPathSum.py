# https://leetcode.com/problems/minimum-falling-path-sum-ii/

# Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero shifts.

# A falling path with non-zero shifts is a choice of exactly one element from each row of grid such that no two elements chosen in adjacent rows are in the same column.


#! Example 1:
# Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
# Output: 13
# Explanation:
# The possible falling paths are:
# [1,5,9], [1,5,7], [1,6,7], [1,6,8],
# [2,4,8], [2,4,9], [2,6,7], [2,6,8],
# [3,4,8], [3,4,9], [3,5,7], [3,5,9]
# The falling path with the smallest sum is [1,5,7], so the answer is 13.

#! Example 2:
# Input: grid = [[7]]
# Output: 7


# Constraints:
# n == grid.length == grid[i].length
# 1 <= n <= 200
# -99 <= grid[i][j] <= 99

# Hint 1
# Use dynamic programming.
# Hint 2
# Let dp[i][j] be the answer for the first i rows such that column j is chosen from row i.
# Hint 3
# Use the concept of cumulative array to optimize the complexity of the solution.

def minFallingPathSum(grid):
    # need to go through all possible combinations
    # brute force - need to check all starting points
    # not valid if the next number is in the same column
    dp = grid[0].copy()
    N = len(grid)
    for r in range(1, N):
        next_row = [float('inf')]*N
        min1 = min2 = float('inf')
        idx1 = -1

        for c in range(N):
            if dp[c] < min1:
                min2 = min1
                min1 = dp[c]
                idx1 = c
            elif dp[c] < min2:
                min2 = dp[c]
        for c in range(N):
            if c == idx1:
                next_row[c] = min2 + grid[r][c]
            else:
                next_row[c] = min1 + grid[r][c]
        dp = next_row
    return min(dp)

#! Example 1:
grid = [[1,2,3],[4,5,6],[7,8,9]]
print(minFallingPathSum(grid))
# Output: 13
# Explanation:
# The possible falling paths are:
# [1,5,9], [1,5,7], [1,6,7], [1,6,8],
# [2,4,8], [2,4,9], [2,6,7], [2,6,8],
# [3,4,8], [3,4,9], [3,5,7], [3,5,9]
# The falling path with the smallest sum is [1,5,7], so the answer is 13.

#! Example 2:
grid = [[7]]
print(minFallingPathSum(grid))
# Output: 7
