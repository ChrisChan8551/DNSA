# Write a function, longest_path, that takes in an adjacency list for a directed acyclic graph. The function should return the length of the longest path within the graph. A path may start and end at any two nodes. The length of a path is considered the number of edges in the path, not the number of nodes.

#! Directed acyclic graph (DAG) - structy way - recursion
def longest_path(graph):
    # Create an empty dictionary called 'distance' to store distances from nodes to the longest path.
    distance = {}

    # Iterate over each node in the graph.
    for node in graph:
        # If the node has no outgoing edges (it's a leaf(terminal) node), set its distance to 0.
        if len(graph[node]) == 0:
            distance[node] = 0

    # Iterate over each node in the graph again.
    for node in graph:
        # Call the 'traverse_distance' function to compute distances for each node and update 'distance' dictionary.
        traverse_distance(graph, node, distance)

    # Return the maximum value from the 'distance' dictionary, which represents the longest path.
    return max(distance.values())

# Define a helper function 'traverse_distance' to recursively compute distances for nodes.


def traverse_distance(graph, node, distance):
    # If the distance for the current node is already computed, return it.
    if node in distance:
        return distance[node]

    # Initialize a variable 'largest' to store the largest distance among neighbors.
    largest = 0

    # Iterate over the neighbors of the current node.
    for neighbor in graph[node]:
        # Recursively call 'traverse_distance' to compute distances for neighbors.
        attempt = traverse_distance(graph, neighbor, distance)

        # Update 'largest' if the computed distance for the neighbor is larger.
        if attempt > largest:
            largest = attempt

    # Calculate the distance for the current node by adding 1 to the largest distance among neighbors.
    distance[node] = 1 + largest

    # Return the computed distance for the current node.
    return distance[node]

#! Dynamic programming algorithm for directed acyclic graph (DAG)
#! It has better performance compared to recursive solution.

# def topological_sort(graph):
#     # Initialize indegree dictionary to count incoming edges for each node
#     indegree = {node: 0 for node in graph}

#     # Calculate indegrees by traversing the graph
#     for node in graph:
#         for neighbor in graph[node]:
#             indegree[neighbor] += 1
#             # print('node: ', node)
#             # print('neighbor: ', neighbor)
#             # print('graph[node]: ', graph[node])
#             # print(indegree)
# #     # Initialize a queue with nodes having indegree 0 (no incoming edges)
#     queue = [node for node, indeg in indegree.items() if indeg == 0]
#     # print('queue: ', queue)
#     topological_order = []  # Initialize the list to store the topological order
#     # print('topological_order: ', topological_order)
# #     # Perform topological sorting
#     while queue:
#         node = queue.pop()
#         # print('node: ', node)
#         topological_order.append(node)
#         # print('topological_order: ', topological_order)

#         # Update indegree for neighbors and enqueue those with indegree 0
#         for neighbor in graph[node]:
#             indegree[neighbor] -= 1
#             if indegree[neighbor] == 0:
#                 queue.append(neighbor)
#         # print(indegree)
#     return topological_order


# def longest_path(graph):
#     top_order = topological_sort(graph)  # Get the topological order of nodes
#     # print('top_order: ', top_order)
#     longest_paths = {node: 0 for node in graph}  # Initialize longest paths dictionary

#     # Calculate longest paths for each node based on predecessors
#     for node in top_order:
#         for neighbor in graph[node]:
#             longest_paths[neighbor] = max(longest_paths[neighbor], longest_paths[node] + 1)

#     # Return the maximum of the longest paths as the longest path in the DAG
#     return max(longest_paths.values())


#! TEST_00
graph = {
    'a': ['c', 'b'],
    'b': ['c'],
    'c': []
}

print(longest_path(graph))  # -> 2

# #! TEST_01
# graph = {
#     'a': ['c', 'b'],
#     'b': ['c'],
#     'c': [],
#     'q': ['r'],
#     'r': ['s', 'u', 't'],
#     's': ['t'],
#     't': ['u'],
#     'u': []
# }

# print(longest_path(graph))  # -> 4

# #! TEST_02
# graph = {
#     'h': ['i', 'j', 'k'],
#     'g': ['h'],
#     'i': [],
#     'j': [],
#     'k': [],
#     'x': ['y'],
#     'y': []
# }

# print(longest_path(graph))  # -> 2

# #! TEST_03
# graph = {
#     'a': ['b'],
#     'b': ['c'],
#     'c': [],
#     'e': ['f'],
#     'f': ['g'],
#     'g': ['h'],
#     'h': []
# }

# print(longest_path(graph))  # -> 3
