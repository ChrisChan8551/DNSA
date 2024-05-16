
# https://leetcode.com/problems/sort-the-matrix-diagonally/description/

# A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For! example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

# Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.


#! Example 1:
# Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
# Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

#! Example 2:
# Input: mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
# Output: [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]


# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# 1 <= mat[i][j] <= 100

#! Hint 1
# Use a data structure to store all values of each diagonal.
#! Hint 2
# How to index the data structure with the id of the diagonal?
#! Hint 3
# All cells in the same diagonal (i,j) have the same difference so we can get the diagonal of a cell using the difference i-j.

from collections import defaultdict


def diagonalSort(mat):
    # we can uniquely identify each diagonal by taking the differences of row and column indices
    # gather diagonal values and assign them into a unique diagonal key
    # sort each of the diagonals
    # replace values in matrix with sorted values
    ROWS, COLS = len(mat), len(mat[0])
    diagonals = defaultdict(list)

    # loop through the matrix to find the diagonals
    for r in range(ROWS):
        for c in range(COLS):
            diag_key = r-c
            # assigning a key to each diagonal
            diagonals[diag_key].append(mat[r][c])

    for diag, values in diagonals.items():
        # sort and reverse so we can use pop on them later
        diagonals[diag] = sorted(values, reverse=True)
    for r in range(ROWS):
        for c in range(COLS):
            mat[r][c] = diagonals[r-c].pop()

    return mat


#! Example 1:
mat = [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]
print(diagonalSort(mat))
# Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

#! Example 2:
mat = [[11, 25, 66, 1, 69, 7], [23, 55, 17, 45, 15, 52], [
    75, 31, 36, 44, 58, 8], [22, 27, 33, 25, 68, 4], [84, 28, 14, 11, 5, 50]]
print(diagonalSort(mat))
# Output: [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]
