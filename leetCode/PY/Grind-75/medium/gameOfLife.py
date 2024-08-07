# https://leetcode.com/problems/game-of-life/

# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

#! Example 1:
# Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

#! Example 2:
# Input: board = [[1,1],[1,0]]
# Output: [[1,1],[1,1]]

# Constraints:
# m == board.length
# n == board[i].length
# 1 <= m, n <= 25
# board[i][j] is 0 or 1.

# Follow up:
# Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?

def gameOfLife(board):
    ROWS, COLS = len(board), len(board[0])
    DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1),
                  (1, 1), (-1, -1), (1, -1), (-1, 1))

    def _inbound(row, col):
        row_inbound = 0 <= row < ROWS
        col_inbound = 0 <= col < COLS
        return row_inbound and col_inbound

    def _living_neighbors(row, col):
        neighbors = 0

        for dr, dc in DIRECTIONS:
            new_row = row+dr
            new_col = col+dc

            if _inbound(new_row, new_col) and board[new_row][new_col] % 2 == 1:
                neighbors += 1
        return neighbors

    for row in range(ROWS):
        for col in range(COLS):
            living_neigh = _living_neighbors(row, col)

            if board[row][col] == 0:
                if living_neigh == 3:
                    board[row][col] = 2
            else:
                if living_neigh < 2 or living_neigh > 3:

                    board[row][col] = 3

    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 3:
                board[row][col] = 0
            elif board[row][col] == 2:
                board[row][col] = 1
    return board

#! Example 1:
board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
print(gameOfLife(board))
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

#! Example 2:
board = [[1, 1], [1, 0]]
print(gameOfLife(board))
# Output: [[1,1],[1,1]]
