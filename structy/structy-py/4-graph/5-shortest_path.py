# Write a function, shortest_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). The function should return the length of the shortest path between A and B. Consider the length as the number of edges in the path, not the number of nodes. If there is no path between A and B, then return -1.

from collections import deque


def shortest_path(edges, node_A, node_B):
    # convert to adjacency list
    graph = {}
    # keep track of visited nodes
    visited = set()
    distance = 0
    # create key-value pairs for each node's adjacency list
    for edge in edges:
        node1, node2 = edge
        if node1 not in graph:
            graph[node1] = []
        if node2 not in graph:
            graph[node2] = []
        graph[node1].append(node2)
        graph[node2].append(node1)

    queue = deque([(node_A, distance)])  # Initialize distance to 0
    visited.add(node_A)

    while queue:
        node, distance = queue.popleft()
        if node == node_B:
            return distance
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                # Increment count for the next level
                queue.append((neighbor, distance + 1))

    return -1  # Return -1 if no path is found


#! TEST_00
edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
]

print(shortest_path(edges, 'w', 'z'))  # -> 2

# #! TEST_01
# edges = [
#     ['w', 'x'],
#     ['x', 'y'],
#     ['z', 'y'],
#     ['z', 'v'],
#     ['w', 'v']
# ]

# print(shortest_path(edges, 'y', 'x'))  # -> 1

# #! TEST_02
# edges = [
#     ['a', 'c'],
#     ['a', 'b'],
#     ['c', 'b'],
#     ['c', 'd'],
#     ['b', 'd'],
#     ['e', 'd'],
#     ['g', 'f']
# ]

# print(shortest_path(edges, 'a', 'e'))  # -> 3

# #! TEST_03
# edges = [
#     ['a', 'c'],
#     ['a', 'b'],
#     ['c', 'b'],
#     ['c', 'd'],
#     ['b', 'd'],
#     ['e', 'd'],
#     ['g', 'f']
# ]

# print(shortest_path(edges, 'e', 'c'))  # -> 2

# #! TEST_04
# edges = [
#     ['a', 'c'],
#     ['a', 'b'],
#     ['c', 'b'],
#     ['c', 'd'],
#     ['b', 'd'],
#     ['e', 'd'],
#     ['g', 'f']
# ]

# print(shortest_path(edges, 'b', 'g'))  # -> -1

# #! TEST_05
# edges = [
#     ['c', 'n'],
#     ['c', 'e'],
#     ['c', 's'],
#     ['c', 'w'],
#     ['w', 'e'],
# ]

# print(shortest_path(edges, 'w', 'e'))  # -> 1

# #! TEST_06
# edges = [
#     ['c', 'n'],
#     ['c', 'e'],
#     ['c', 's'],
#     ['c', 'w'],
#     ['w', 'e'],
# ]

# print(shortest_path(edges, 'n', 'e'))  # -> 2

# #! TEST_07
# edges = [
#     ['m', 'n'],
#     ['n', 'o'],
#     ['o', 'p'],
#     ['p', 'q'],
#     ['t', 'o'],
#     ['r', 'q'],
#     ['r', 's']
# ]

# print(shortest_path(edges, 'm', 's'))  # -> 6
