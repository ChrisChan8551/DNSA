# Write a function, minimum_island, that takes in a grid containing Ws and Ls. W represents water and L represents land. The function should return the size of the smallest island. An island is a vertically or horizontally connected region of land.

# You may assume that the grid contains at least one island.
from collections import deque

#! Breadth-first my way


def minimum_island(grid):
    # edge case if grid is empty
    if not grid:
        return 0
    # assign visited to keep track of the nodes that have been visited
    visited = set()
    # assign variables to keep track of minimum size island
    min_island = float('inf')
    # assign variable to keep track of minimum size of the island
    # will need to assign coords row and col
    # iterate through the grid to find the "L" to indicate the land
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            # if L is found, explorer the island and count nodes, also check if the nodes are not in visited
            if grid[row][col] == 'L' and (row, col) not in visited:
                # reset count to inf when there's a new island
                # visited.add(grid[row][col])
                island_count = explore(grid, (row, col), visited)
                # print('island_count: ', island_count)
                min_island = min(min_island, island_count)
                # print('visited: ', visited)
    return min_island


def explore(grid, start, visited):
    # print('start: ', start)
    # print('start: ', start)
    queue = deque([start])
    visited.add(start)
    # assign variables for the directions
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    # assign a count to keep track of size of the island
    count = 1
    while queue:
        # deconstruct the queue to get the row col coords
        row, col = queue.popleft()
        # print('row: ', row, 'col: ', col)
        #     # make a look and add directions to the row and cols
        for drow, dcol in directions:
            new_row, new_col = row + drow, col + dcol
            # print('new row: ', new_row, 'new col: ', new_col)
            # valid nodes are only directly above,below, left, and right by 1 node.
            # need to check if the node is within the grid boundries
            if (
                # check if within the grid boundries
                0 <= new_row < len(grid)
                and 0 <= new_col < len(grid[row])
                # need to check if they are in the visited
                and (new_row, new_col) not in visited
                # check if nodes are L
                and grid[new_row][new_col] == 'L'
            ):
                # increase count if node is valid
                count += 1
                # print('count :', count)

                # add coords to viisted and queue
                visited.add((new_row, new_col))
                queue.append((new_row, new_col))
            # print('before min_island :', min_island)
            # print('final count:', count)
            # print('after min_island :', min_island)
    # print('final count:', count)
    # print('exit explore')
    return count

#! Depth first


def minimum_island(grid):
    visited = set()
    min_size = float("inf")
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size = explore_size(grid, r, c, visited)
            if size > 0 and size < min_size:
                min_size = size
    return min_size


def explore_size(grid, r, c, visited):
    row_inbounds = 0 <= r < len(grid)
    col_inbounds = 0 <= c < len(grid[0])
    if not row_inbounds or not col_inbounds:
        return 0

    if grid[r][c] == 'W':
        return 0

    pos = (r, c)
    if pos in visited:
        return 0
    visited.add(pos)

    size = 1
    size += explore_size(grid, r - 1, c, visited)
    size += explore_size(grid, r + 1, c, visited)
    size += explore_size(grid, r, c - 1, visited)
    size += explore_size(grid, r, c + 1, visited)
    return size


#! TEST_00
grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
]

print(minimum_island(grid))  # -> 2


#! TEST_01
grid = [
    ['L', 'W', 'W', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['W', 'L', 'W', 'L', 'W'],
    ['W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'L', 'L', 'L'],
]

print(minimum_island(grid))  # -> 1

#! TEST_02
grid = [
    ['L', 'L', 'L'],
    ['L', 'L', 'L'],
    ['L', 'L', 'L'],
]

print(minimum_island(grid))  # -> 9

#! TEST_03
grid = [
    ['W', 'W'],
    ['L', 'L'],
    ['W', 'W'],
    ['W', 'L']
]

print(minimum_island(grid))  # -> 1
