# Write a function, connected_components_count, that takes in the adjacency list of an undirected graph. The function should return the number of connected components within the graph.

from collections import deque

#! depth first
# def connected_components_count(graph):
#     # iterate through the list using depth or breadth traversal
#     # mark off visited nodes
#     visited = set()
#     # keep a count for number of components and increase the count for each component
#     count = 0
#     # explore each node the nodes will be the [key]
#     for node in graph:
#         if explore(graph, node, visited) == True:
#             count += 1
#     return count


# def explore(graph, current, visited):
#     # base case to check if the current node is visited
#     if current in visited:
#         # return boolean indicating whether the current node is visited
#         return False
#     # if not visited then add to visited set
#     visited.add(current)
#     # recursively to check through nodes.
#     for neighbor in graph[current]:
#         explore(graph, neighbor, visited)

#     return True

#!longer convoluted way
def connected_components_count(graph):
    visited = set()
    count = 0
    for node in graph:
        print('node :', node)
        if node not in visited:
            count += 1
            queue = deque([node])
            while queue:
                current = queue.popleft()
                if current not in visited:
                    visited.add(current)
                    for neighbor in graph[current]:
                        if neighbor not in visited:
                            queue.append(neighbor)
    return count


#! TEST_00
print(connected_components_count({
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}))  # -> 2

# #! TEST_01
# print(connected_components_count({
#     1: [2],
#     2: [1, 8],
#     6: [7],
#     9: [8],
#     7: [6, 8],
#     8: [9, 7, 2]
# }))  # -> 1

# #! TEST_02
# print(connected_components_count({
#     3: [],
#     4: [6],
#     6: [4, 5, 7, 8],
#     8: [6],
#     7: [6],
#     5: [6],
#     1: [2],
#     2: [1]
# }))  # -> 3

# #! TEST_03
# print(connected_components_count({}))  # -> 0

# #! TEST_04
# print(connected_components_count({
#     0: [4, 7],
#     1: [],
#     2: [],
#     3: [6],
#     4: [0],
#     6: [3],
#     7: [0],
#     8: []
# }))  # -> 5
