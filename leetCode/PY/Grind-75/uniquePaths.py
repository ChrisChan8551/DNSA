# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

# Example 1:


# Input: m = 3, n = 7
# Output: 28
# Example 2:

# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down


# Constraints:

# 1 <= m, n <= 100

def uniquePaths(m, n):
    def path_count(m, n):
        if m == 0 or n == 0:
            return 0
        elif m == 1 and n == 1:
            return 1
        return path_count(m-1, n) + path_count(m, n-1)
    return path_count(m, n)

#! chatGPT
def uniquePaths(m, n):
    # Create a 2D array to store the number of unique paths
    dp = [[0] * n for _ in range(m)]

    # Initialize the top row and left column to 1 (only one way to reach each cell in the top row and left column)
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1

    # Fill in the rest of the array by summing the values from the cell above and the cell to the left
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    # The bottom-right cell now contains the number of unique paths
    return dp[-1][-1]

print(uniquePaths(3, 7))
print(uniquePaths(3, 2))
