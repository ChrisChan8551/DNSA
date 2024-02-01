# Write a function, closest_carrot, that takes in a grid, a starting row, and a starting column. In the grid, 'X's are walls, 'O's are open spaces, and 'C's are carrots. The function should return a number representing the length of the shortest path from the starting position to a carrot. You may move up, down, left, or right, but cannot pass through walls (X). If there is no possible path to a carrot, then return -1.
from collections import deque

#! breadth-first


def closest_carrot(grid, starting_row, starting_col):
    visited = set()
    start = (starting_row, starting_col)
    # difference betwee this excercise is now you have to track the distance. Add the distance to the starting coords.
    # starting distance to be set as 1
    queue = deque([(start, 0)])
    visited.add(start)
    # check only up, down, left, right. diagonals are not allowed.
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    # initiate the BFS
    while queue:
        # destructure row, col, and distance from the starting point.
        (row, col), distance = queue.popleft()
        if (grid[row][col] == 'C'):
            return distance
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if (
                0 <= new_row < len(grid)
                and 0 <= new_col < len(grid[row])
                and (new_row, new_col) not in visited
                # need to avoid 'X' or walls
                and grid[new_row][new_col] != 'X'
            ):
                visited.add((new_row, new_col))
                # add to distance if C is not found
                queue.append(((new_row, new_col), distance + 1))
    return -1


#! TEST_00
grid = [
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'X', 'O', 'O', 'O'],
    ['O', 'X', 'X', 'O', 'O'],
    ['O', 'X', 'C', 'O', 'O'],
    ['O', 'X', 'X', 'O', 'O'],
    ['C', 'O', 'O', 'O', 'O'],
]

print(closest_carrot(grid, 1, 2))  # -> 4

# #! TEST_01
# grid = [
#     ['O', 'O', 'O', 'O', 'O'],
#     ['O', 'X', 'O', 'O', 'O'],
#     ['O', 'X', 'X', 'O', 'O'],
#     ['O', 'X', 'C', 'O', 'O'],
#     ['O', 'X', 'X', 'O', 'O'],
#     ['C', 'O', 'O', 'O', 'O'],
# ]

# print(closest_carrot(grid, 0, 0))  # -> 5

# #! TEST_02
# grid = [
#     ['O', 'O', 'X', 'X', 'X'],
#     ['O', 'X', 'X', 'X', 'C'],
#     ['O', 'X', 'O', 'X', 'X'],
#     ['O', 'O', 'O', 'O', 'O'],
#     ['O', 'X', 'X', 'X', 'X'],
#     ['O', 'O', 'O', 'O', 'O'],
#     ['O', 'O', 'C', 'O', 'O'],
#     ['O', 'O', 'O', 'O', 'O'],
# ]

# print(closest_carrot(grid, 3, 4))  # -> 9

# #! TEST_03
# grid = [
#     ['O', 'O', 'X', 'O', 'O'],
#     ['O', 'X', 'X', 'X', 'O'],
#     ['O', 'X', 'C', 'C', 'O'],
# ]

# print(closest_carrot(grid, 1, 4))  # -> 2

# #! TEST_04
# grid = [
#     ['O', 'O', 'X', 'O', 'O'],
#     ['O', 'X', 'X', 'X', 'O'],
#     ['O', 'X', 'C', 'C', 'O'],
# ]

# print(closest_carrot(grid, 2, 0))  # -> -1

# #! TEST_05
# grid = [
#     ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
#     ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
#     ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
#     ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
#     ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
#     ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
#     ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
#     ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
#     ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
#     ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
#     ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X'],
#     ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'C'],
# ]

# print(closest_carrot(grid, 0, 0))  # -> -1

# #! TEST_06
# grid = [
#     ['O', 'O', 'X', 'C', 'O'],
#     ['O', 'X', 'X', 'X', 'O'],
#     ['C', 'X', 'O', 'O', 'O'],
# ]

# print(closest_carrot(grid, 2, 2))  # -> 5
