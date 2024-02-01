# There is a rectangular brick wall in front of you with n rows of bricks. The ith row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.

# Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

# Given the 2D array wall that contains the information about the wall, return the minimum number of crossed bricks after drawing such a vertical line.

# Example 1:


# Input: wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
# Output: 2
# Example 2:

# Input: wall = [[1],[1],[1]]
# Output: 3


# Constraints:

# n == wall.length
# 1 <= n <= 104
# 1 <= wall[i].length <= 104
# 1 <= sum(wall[i].length) <= 2 * 104
# sum(wall[i]) is the same for each row i.
# 1 <= wall[i][j] <= 231 - 1

def leastBricks(wall):
    # total width of the wall is fixed
    # how to deal with varying lengths of the bricks?
    # iterate through the rows and visualize each unit of brick as an index
    # we do not need to count index 0 or index length of row
    # use hash map to keep track of how many gaps there are for each index
    # return length minus max number of gaps

    gapCount = {}  # key: val -> index: # of gaps

    for row in wall:
        total = 0
        # Note: Exclude the last brick in each row
        for brick in row[:-1]:
            total += brick
            gapCount.setdefault(total, 0)
            gapCount[total] += 1

    gapValues = gapCount.values()
    return len(wall) - max(gapValues, default=0)


print(leastBricks([[1, 2, 2, 1], [3, 1, 2], [
      1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]))  # -> 2

print(leastBricks([[1], [1], [1]]))  # -> 3
