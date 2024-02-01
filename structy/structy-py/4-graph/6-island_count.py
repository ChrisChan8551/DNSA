# Write a function, island_count, that takes in a grid containing Ws and Ls. W represents water and L represents land. The function should return the number of islands on the grid. An island is a vertically or horizontally connected region of land.
from collections import deque


#! Breadth-first solution
def island_count(grid):
    # Check for the edge case if the grid is empty.
    if not grid:
        return 0

    # Initialize the island count and a set to keep track of visited positions.
    island_count = 0
    visited = set()

    # Iterate through each row in the grid.
    for row in range(len(grid)):
        # Iterate through each column in the current row.
        for col in range(len(grid[row])):
            # If the current cell is unvisited land ('L'), start exploring the island.
            if grid[row][col] == 'L' and (row, col) not in visited:
                # Call the explore function to explore the island.
                explore(grid, (row, col), visited)
                # Increment the island count for each new island found.
                island_count += 1

    return island_count

# Define a helper function to explore the connected region of land using BFS.


def explore(grid, start, visited):
    # Initialize a queue for BFS and add the starting position to it.
    queue = deque([start])
    # Mark the starting position as visited.
    visited.add(start)
    # Define possible directions to move: up, down, left, and right.
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Continue BFS until the queue is empty.
    while queue:
        # Get the current position from the queue.
        row, col = queue.popleft()
        # Check all possible directions to move.
        for dr, dc in directions:
            # Calculate the new position.
            new_row, new_col = row + dr, col + dc
            # Check if the new position is within the grid boundaries, unvisited, and is land ('L').
            if (
                0 <= new_row < len(grid)
                and 0 <= new_col < len(grid[0])
                and (new_row, new_col) not in visited
                and grid[new_row][new_col] == 'L'
            ):
                # Mark the new position as visited and add it to the queue for further exploration.
                visited.add((new_row, new_col))
                queue.append((new_row, new_col))

#! Depth first


def island_count(grid):
    # Initialize a set to keep track of visited positions.
    visited = set()
    # Initialize a variable to count the number of islands.
    count = 0
    # Iterate through each row in the grid.
    for row in range(len(grid)):
        # Iterate through each column in the current row.
        for col in range(len(grid[0])):
            # If the explore function returns True for the current cell, it's part of an island.
            if explore(grid, row, col, visited) == True:
                # Increment the island count.
                count += 1
    # Return the total count of islands.
    return count

# Define a helper function to explore the connected region of land using DFS.


def explore(grid, row, col, visited):
    # Check if the current row is within the grid boundaries.
    row_inbounds = 0 <= row < len(grid)
    # Check if the current column is within the grid boundaries.
    col_inbounds = 0 <= col < len(grid[0])

    # If either row or column is out of bounds, return False, indicating it's not part of an island.
    if not row_inbounds or not col_inbounds:
        return False

    # If the current cell is water ('W'), return False, indicating it's not part of an island.
    if grid[row][col] == 'W':
        return False

    # Create a tuple representing the current position.
    pos = (row, col)

    # If the current position is already visited, return False.
    if pos in visited:
        return False

    # Mark the current position as visited.
    visited.add(pos)

    # Recursively explore neighboring positions (up, down, left, right).
    explore(grid, row - 1, col, visited)  # Up
    explore(grid, row + 1, col, visited)  # Down
    explore(grid, row, col - 1, visited)  # Left
    explore(grid, row, col + 1, visited)  # Right

    # Return True, indicating that the current cell is part of an island.
    return True


#! TEST_00
grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
]

print(island_count(grid))  # -> 3

#! TEST_01
grid = [
    ['L', 'W', 'W', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['W', 'L', 'W', 'L', 'W'],
    ['W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'L', 'L', 'L'],
]

print(island_count(grid))  # -> 4

#! TEST_02
grid = [
    ['L', 'L', 'L'],
    ['L', 'L', 'L'],
    ['L', 'L', 'L'],
]

print(island_count(grid))  # -> 1

#! TEST_03
grid = [
    ['W', 'W'],
    ['W', 'W'],
    ['W', 'W'],
]

print(island_count(grid))  # -> 0
