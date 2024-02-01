# Write a function, undirected_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). The function should return a boolean indicating whether or not there exists a path between node_A and node_B.


# #! depth first
# def undirected_path(edges, node_A, node_B):
#     # convert edges to adjacency lists
#     graph = {}
#     # will need to keep track of visisted nodes in a undirected graph using a set
#     visited = set()

#     # create key value pairs for each edge
#     for edge in edges:
#         node1, node2 = edge
#         # checks if node1 is already in the graph dictionary. If not, it adds node1 as a key in the graph dictionary with an empty list as its associated value.
#         if node1 not in graph:
#             graph[node1] = []
#         if node2 not in graph:
#             graph[node2] = []
#         # each node stores a list of its neighboring nodes, representing the edges in the graph.
#         graph[node1].append(node2)
#         graph[node2].append(node1)
#     # depth first traversal
#     # graph
#     # {
#     # i: [j,k]
#     # j: [i],
#     # k: [i,m,l]
#     # m: [k]
#     # l:[k]
#     # o: [n]
#     # n:[o]
#     # }

#     def has_path(node):
#         if node == node_B:
#             return True
#         visited.add(node)
#         for neighbor in graph.get(node, []):
#             # .get(node, []): The .get() method of a dictionary is used to retrieve the value associated with a key (node in this case). If the key is not found in the dictionary (i.e., the node has no neighbors), it returns an empty list [] as the default value.
#             # For each unvisited neighbor, recursively call DFS.
#             if neighbor not in visited:
#                 if has_path(neighbor):
#                     return True
#         return False

#     # Start DFS from node_A.
#     return has_path(node_A)
#     #! edge case - need to watch out nodes that 'cycle' (nodes that have a circle and goes into infinity)
#     #! edge case - when nodes are disconnected from the main graph (not part of the main graph)


#! breadth first
from collections import deque


def undirected_path(edges, node_A, node_B):
    # Create a dictionary to represent the undirected graph.
    graph = {}
    for edge in edges:
        node1, node2 = edge
        if node1 not in graph:
            graph[node1] = []
        if node2 not in graph:
            graph[node2] = []
        graph[node1].append(node2)
        graph[node2].append(node1)

    # Create a queue for BFS and initialize it with node_A.
    queue = deque([node_A])

    # Create a set to keep track of visited nodes during BFS.
    visited = set()

    # Start BFS.
    while queue:
        node = queue.popleft()

        # If the current node is node_B, a path has been found.
        if node == node_B:
            return True

        # Mark the current node as visited.
        visited.add(node)

        # Add unvisited neighbors to the queue for exploration.
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                queue.append(neighbor)

    # If no path is found after BFS, return False.
    return False


#! TEST_00
edges = [
    ('i', 'j'),
    ('k', 'i'),
    ('m', 'k'),
    ('k', 'l'),
    ('o', 'n')
]

print(undirected_path(edges, 'j', 'm'))  # -> True

# #! TEST_01
# edges = [
#     ('i', 'j'),
#     ('k', 'i'),
#     ('m', 'k'),
#     ('k', 'l'),
#     ('o', 'n')
# ]

# print(undirected_path(edges, 'm', 'j'))  # -> True

# #! TEST_02
# edges = [
#     ('i', 'j'),
#     ('k', 'i'),
#     ('m', 'k'),
#     ('k', 'l'),
#     ('o', 'n')
# ]

# print(undirected_path(edges, 'l', 'j'))  # -> True

# #! TEST_03
# edges = [
#     ('i', 'j'),
#     ('k', 'i'),
#     ('m', 'k'),
#     ('k', 'l'),
#     ('o', 'n')
# ]

# print(undirected_path(edges, 'k', 'o'))  # -> False

# #! TEST_04
# edges = [
#     ('i', 'j'),
#     ('k', 'i'),
#     ('m', 'k'),
#     ('k', 'l'),
#     ('o', 'n')
# ]

# print(undirected_path(edges, 'i', 'o'))  # -> False

# #! TEST_05
# edges = [
#     ('b', 'a'),
#     ('c', 'a'),
#     ('b', 'c'),
#     ('q', 'r'),
#     ('q', 's'),
#     ('q', 'u'),
#     ('q', 't'),
# ]


# print(undirected_path(edges, 'a', 'b'))  # -> True

# #! TEST_06
# edges = [
#     ('b', 'a'),
#     ('c', 'a'),
#     ('b', 'c'),
#     ('q', 'r'),
#     ('q', 's'),
#     ('q', 'u'),
#     ('q', 't'),
# ]

# print(undirected_path(edges, 'a', 'c'))  # -> True

# #! TEST_07
# edges = [
#     ('b', 'a'),
#     ('c', 'a'),
#     ('b', 'c'),
#     ('q', 'r'),
#     ('q', 's'),
#     ('q', 'u'),
#     ('q', 't'),
# ]

# print(undirected_path(edges, 'r', 't'))  # -> True

# #! TEST_08
# edges = [
#     ('b', 'a'),
#     ('c', 'a'),
#     ('b', 'c'),
#     ('q', 'r'),
#     ('q', 's'),
#     ('q', 'u'),
#     ('q', 't'),
# ]

# print(undirected_path(edges, 'r', 'b'))  # -> False

# #! TEST_09
# edges = [
#     ('s', 'r'),
#     ('t', 'q'),
#     ('q', 'r'),
# ]

# print(undirected_path(edges, 'r', 't'))  # -> True
