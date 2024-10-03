# https://leetcode.com/problems/spiral-matrix-iii/

# You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.

# You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid.

# Return an array of coordinates representing the positions of the grid in the order you visited them.


#! Example 1:
# Input: rows = 1, cols = 4, rStart = 0, cStart = 0
# Output: [[0,0],[0,1],[0,2],[0,3]]

#! Example 2:
# Input: rows = 5, cols = 6, rStart = 1, cStart = 4
# Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]


# Constraints:

# 1 <= rows, cols <= 100
# 0 <= rStart < rows
# 0 <= cStart < cols

def spiralMatrixIII(rows, cols, rStart, cStart):
    # guaranteed to start within bounds
    # guaranteed to at least be a 1 x 1 (no empty grid)
    # spiral outwards in clockwise direction
    # record all cells that we traverse within bounds
    # directions array would be useful
    # keep track of positions visited in visited set
    # not necessary since we are already guaranteed to never revisit cells
    # check for inbounds to see whether we need to record it in our output or not

    # how wdo we know when we have traversed all cells?
    # when number of cells == rol * col
    # when do we switch direction?
    # start with 1 step
    # increase num of steps per direction when we got left or right
    # right, down, left, up (order matters)

    DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
    d = 0
    results = [[rStart, cStart]]
    steps = 0
    r, c = rStart, cStart
    # nr = r + DIRECTIONS[d][0]
    # nc = c + DIRECTIONS[d][1]

    def _inbound(r, c):
        r_inbound = 0 <= r < rows
        c_inbound = 0 <= c < cols
        return r_inbound and c_inbound

    while len(results) < rows * cols:
        # increment steps if d is in left or right directions
        if d % 2 == 0:
            steps += 1

        for i in range(steps):
            dr, dc = DIRECTIONS[d][0], DIRECTIONS[d][1]
            r = r + dr
            c = c + dc
            if _inbound(r, c):
                results.append([r, c])
        d += 1
        if d == 4:
            d = 0

    return results


#! Example 1:
rows = 1
cols = 4
rStart = 0
cStart = 0
print(spiralMatrixIII(rows, cols, rStart, cStart))
# Output: [[0,0],[0,1],[0,2],[0,3]]

#! Example 2:
rows = 5
cols = 6
rStart = 1
cStart = 4
print(spiralMatrixIII(rows, cols, rStart, cStart))
# Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
