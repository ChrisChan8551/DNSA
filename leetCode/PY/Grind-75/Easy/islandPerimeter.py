# https://leetcode.com/problems/island-perimeter/

# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.


# !Example 1:
# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.

# !Example 2:
# Input: grid = [[1]]
# Output: 4

# !Example 3:
# Input: grid = [[1,0]]
# Output: 4


# Constraints:
# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 100
# grid[i][j] is 0 or 1.
# There is exactly one island in grid.


def islandPerimeter(grid):
    # find the island, then DFS to find how far the island goes
    # save how many neighbors an island has?
    # keep track of perimeter count
    # increment each time we hit water or out of bounds
    # DFS base case
    # keep track of visited cells using a set

    ROWS, COLS = len(grid), len(grid[0])

    def _dfs():
        # base case
        if not _inbound(r, c):
            return 1
        if (row, col) in visited:
            return 0

        visited.add((r, c))
        return _dfs(r-1, c) + _dfs(r, c-1) + _dfs(r+1, c) + _dfs(r, c+1)

    def _inbound(r, c):
        row_inbound = 0 <= r < ROWS
        col_inbound = 0 <= c < COLS
        return row_inbound and col_inbound

    visited = set()
    # traverse through the grid and look for 1
    for r in range(ROWS):
        for c in range(COL):
            if grid[r][c] == 1:
                _dfs(r, c)

    return


# !Example 1:
grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
print(islandPerimeter(grid))
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.

# !Example 2:
grid = [[1]]
print(islandPerimeter(grid))
# Output: 4

# !Example 3:
grid = [[1, 0]]
print(islandPerimeter(grid))
# Output: 4
