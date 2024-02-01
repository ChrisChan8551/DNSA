# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.


# Example 1:


# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
# Example 2:

# Input: n = 1
# Output: [["Q"]]


# Constraints:

# 1 <= n <= 9

def solveNQueens(n):
    res = []
    # create the board
    board = [['.']*n for _ in range(n)]

    col = set()
    neg_diag = set()  # r - c (pattern for diagonals)
    pos_diag = set()  # r + c

    print(board)

    def _backtrack(r):
        if r == n:
            copy = [''.join(row)for row in board]
            res.append(copy)
            return

        for c in range(n):
            if c not in col and (r+c) not in pos_diag and (r-c) not in neg_diag:
                # modify state
                board[r][c] = 'Q'
                col.add(c)
                neg_diag.add(r-c)
                pos_diag.add(r+c)
                # attempt path

                _backtrack(r+1)

                # undo modification
                board[r][c] = '.'
                col.discard(c)
                neg_diag.discard(r-c)
                pos_diag.discard(r+c)
                # add to our res with backtracking

    _backtrack(0)
    return res
# only 1 queen per row
# back tracking - find all possible solutions
# run every possibility until...
    # 1) find a valid solution
    # 2) no other solution or possible path
    # 3) recursive
# steps
    # modify state
    # try this path
    # backtrack (undo modified state)
# valid moves
    # not in the same row
    # not in the same col
    # not in the same positive diagonal
    # not in the same negative diagonal
#


print(solveNQueens(4))
print(solveNQueens(1))
