# https://leetcode.com/problems/valid-sudoku/
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# Constraints:
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.

from collections import defaultdict


def subBox(board):
    return


def isValidSudoku(board):
    # check if there are any duplicates in row, cols, and subboxes
    # rows = subarray
    # store values in a data structure
    # using a set will allow us to check for unique values
    # will need to use a set for each row, col, subbox.
    # check for conflicts as we add numbers into the sets
    # if there is a conflict return false
    # return True if we can go through entire matrix without conflicts
    # the start of every subbox is every 3 spaces.

    # preassign set and populate for the grid
    row = [set() for _ in range(9)]
    col = [set() for _ in range(9)]
    box = defaultdict(set)
    for r in range(9):
        for c in range(9):
            current_value = board[r][c]

            if current_value == '.':
                continue

            box_coord = f'{r//3},{c//3}'

            # check if value exists in the set while traversing the grid
            if current_value in row[r] or current_value in col[c] or current_value in box[box_coord]:
                return False
            # if no value exists then add to grid
            row[r].add(current_value)
            col[c].add(current_value)
            box[box_coord].add(current_value)

    return True


#! Example 1:
# board = [
#     ["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".",
#                                                                                                                                                                                                  "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]
# ]
# print(isValidSudoku(board))
# Output: true
# #! Example 2:
# board = [
#     ["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
# print(isValidSudoku(board))
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
# #! Example 3:
# board = [
#     ["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
# print(isValidSudoku(board))
#! Example 4:
board = [
    [".", ".", ".", ".", "5", ".", ".", "1", "."],
    [".", "4", ".", "3", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "3", ".", ".", "1"],
    ["8", ".", ".", ".", ".", ".", ".", "2", "."],
    [".", ".", "2", ".", "7", ".", ".", ".", "."],
    [".", "1", "5", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "2", ".", ".", "."],
    [".", "2", ".", "9", ".", ".", ".", ".", "."],
    [".", ".", "4", ".", ".", ".", ".", ".", "."]
]
r, c = 0, 3
print(subBox(board))
# print(isValidSudoku(board))
# print(subBox(board))
