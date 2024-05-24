# https://leetcode.com/problems/largest-local-values-in-a-matrix/


# You are given an n x n integer matrix grid.

# Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:

# maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
# In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

# Return the generated matrix.


# Example 1:


# Input: grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
# Output: [[9,9],[8,6]]
# Explanation: The diagram above shows the original matrix and the generated matrix.
# Notice that each value in the generated matrix corresponds to the largest value of a contiguous 3 x 3 matrix in grid.
# Example 2:


# Input: grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
# Output: [[2,2,2],[2,2,2],[2,2,2]]
# Explanation: Notice that the 2 is contained within every contiguous 3 x 3 matrix in grid.


# Constraints:

# n == grid.length == grid[i].length
# 3 <= n <= 100
# 1 <= grid[i][j] <= 100

# #! brute force - O(n^2 * m^2)
# def largestLocal(grid):
#     n = len(grid)
#     result = []

#     for i in range(n - 2):
#         row = []
#         for j in range(n - 2):
#             maxSum = 0
#             # row.append(grid[i][j])
#             # print('row: ', row)
#             for x in range(i, i + 3):
#                 for y in range(j, j + 3):
#                     maxSum = max(maxSum, grid[x][y])

#             row.append(maxSum)
#         result.append(row)
#     return result


# def largestLocal(grid):
#     n = len(grid)
#     result = []

#     for i in range(n - 2):
#         row = []
#         for j in range(n - 2):
#             maxSum = grid[i][j]

#             for x in range(3):
#                 for y in range(3):
#                     maxSum = max(maxSum, grid[i+x][j+y])

#             row.append(maxSum)
#         result.append(row)
#     return result

#! Optimized O(n^2)
def largestLocal(grid):
    n = len(grid)
    # Step 1: Compute horizontal max for each row
    horizontal_max = [[0] * (n - 2) for _ in range(n)]

    for i in range(n):
        for j in range(n - 2):
            horizontal_max[i][j] = max(
                grid[i][j], grid[i][j + 1], grid[i][j + 2])

    # Step 2: Compute vertical max using horizontal max
    maxLocal = [[0] * (n - 2) for _ in range(n - 2)]

    for i in range(n - 2):
        for j in range(n - 2):
            maxLocal[i][j] = max(
                horizontal_max[i][j], horizontal_max[i + 1][j], horizontal_max[i + 2][j])

    return maxLocal


print(largestLocal([[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]))
# Output: [[9,9],[8,6]]
# Explanation: The diagram above shows the original matrix and the generated matrix.
# Notice that each value in the generated matrix corresponds to the largest value of a contiguous 3 x 3 matrix in grid.

# print(largestLocal([[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]))
# Output: [[2,2,2],[2,2,2],[2,2,2]]
# Explanation: Notice that the 2 is contained within every contiguous 3 x 3 matrix in grid.
