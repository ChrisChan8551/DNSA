# Write a function, has_path, that takes in a dictionary representing the adjacency list of a directed acyclic graph and two nodes (src, dst). The function should return a boolean indicating whether or not there exists a directed path between the source and destination nodes.
from collections import deque

#!breadth first


def has_path(graph, src, dst):
    queue = deque([src])
    while queue:
        current = queue[0]
        if current == dst:
            return True
        queue.popleft()
        for neighbor in graph[current]:
            queue.append(neighbor)
    return False

#! depth first
# Check if there is a path from the source node 'src' to the destination node 'dst' in the graph.


def has_path(graph, src, dst):
    # If the source and destination nodes are the same, there is a path (base case).
    if src == dst:
        return True

    # Iterate through the neighbors of the source node in the graph.
    for neighbor in graph[src]:
        # Recursively check if there is a path from the neighbor to the destination node.
        # If a path is found (recursive call returns True), return True.
        if has_path(graph, neighbor, dst) == True:
            return True

    # If no path is found after checking all neighbors, return False.
    return False


#! TEST_00
graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}

print(has_path(graph, 'f', 'k'))  # True

# #! TEST_01
# graph = {
#     'f': ['g', 'i'],
#     'g': ['h'],
#     'h': [],
#     'i': ['g', 'k'],
#     'j': ['i'],
#     'k': []
# }

# print(has_path(graph, 'f', 'j'))  # False

# #! TEST_02
# graph = {
#     'f': ['g', 'i'],
#     'g': ['h'],
#     'h': [],
#     'i': ['g', 'k'],
#     'j': ['i'],
#     'k': []
# }

# print(has_path(graph, 'i', 'h'))  # True

# #! TEST_03
# graph = {
#     'v': ['x', 'w'],
#     'w': [],
#     'x': [],
#     'y': ['z'],
#     'z': [],
# }

# print(has_path(graph, 'v', 'w'))  # True

# #! TEST_04
# graph = {
#     'v': ['x', 'w'],
#     'w': [],
#     'x': [],
#     'y': ['z'],
#     'z': [],
# }

# print(has_path(graph, 'v', 'z'))  # False
