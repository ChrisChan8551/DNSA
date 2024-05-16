# https://leetcode.com/problems/number-of-islands/

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


#! Example 1:
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

#! Example 2:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3


# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.


def numIslands(grid):
    # islands are connecting horizontal or vertical from starting point
    # does not count diagonals
    # transverse grid, and look for 1, then DFS to find the entirety of the island
    # we can change the 1s to a 0 so that we don't have to use a set
    # use a count variable to keep track of islands

    # loop through the grid, and look for a 1.
    # once a 1 is found, need to look at top, bottom, left, right to check for other 1s
    ROWS, COLS = len(grid), len(grid[0])
    DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))
    count = 0

    def _inbound(row, col):
        row_inbound = 0 <= row < ROWS
        col_inbound = 0 <= col < COLS
        return row_inbound and col_inbound

    def _dfs(row, col):
        if not _inbound(row, col) or grid[row][col] == '0':
            return

        # equivalent to using a set. Changing visited island to 0
        grid[row][col] = '0'

        # check all the neighbors
        for dr, dc in DIRECTIONS:
            _dfs(row + dr, col + dc)

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == '1':
                _dfs(r, c)
                count += 1
    # loop through the grid and identify the 1s

    return count


#! Example 1:
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

print(numIslands(grid))
# Output: 1

#! Example 2:
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(numIslands(grid))
# Output: 3
