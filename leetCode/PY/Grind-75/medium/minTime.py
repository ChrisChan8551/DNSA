# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/

# Given an undirected tree consisting of n vertices numbered from 0 to n-1, which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. Return the minimum time in seconds you have to spend to collect all apples in the tree, starting at vertex 0 and coming back to this vertex.

# The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi. Additionally, there is a boolean array hasApple, where hasApple[i] = true means that vertex i has an apple; otherwise, it does not have any apple.


# Example 1:
# Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false]
# Output: 8
# Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.

# Example 2:
# Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,false,true,false]
# Output: 6
# Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.

# Example 3:
# Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,false,false,false,false,false]
# Output: 0


# Constraints:

# 1 <= n <= 105
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai < bi <= n - 1
# hasApple.length == n

# Hint 1
# Note that if a node u contains an apple then all edges in the path from the root to the node u have to be used forward and backward (2 times).
# Hint 2
# Therefore use a depth-first search (DFS) to check if an edge will be used or not.

from collections import defaultdict


# def minTime(n, edges, hasApple):
#     # traverse tree to get all apples
#     # needs to return to vertex 0 at the end
#     # DFS to search tree
#     #! This is not a binary tree. It's a graph.
#     # convert edges into adjacency list to more easily manage
#     graph = defaultdict(list)
#     visited = set()
#     for a, b in edges:
#         # need to setup both ways because it's undirected tree
#         graph[a].append(b)
#         graph[b].append(a)

#     def _dfs(node):
#         if node in visited:
#             return 0

#         visited.add(node)
#         seconds = 0

#         # process node - traverse all neighbors as there's multiple possible neighbors.

#         for child in graph[node]:
#             seconds += _dfs(child)

#         # checking if there are apples in children subtrees
#         if seconds > 0:
#             if node == 0:
#                 return seconds
#             else:
#                 return seconds + 2
#         # if there are no apples below, check current node for an apple
#         return 2 if hasApple[node] and node != 0 else 0

#     return _dfs(0)

def minTime(n, edges, hasApple):
    # Create an adjacency list for the tree
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)

    # Depth-First Search to calculate the minimum time
    def dfs(node, parent):
        total_time = 0
        for child in tree[node]:
            if child == parent:
                continue
            child_time = dfs(child, node)
            # If the child has an apple or there are apples in its subtree, add 2 seconds (1 second each way)
            if child_time > 0 or hasApple[child]:
                total_time += child_time + 2
        return total_time

    return dfs(0, -1)


#! Example 1:
n = 7
edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
hasApple = [False, False, True, False, True, True, False]
print(minTime(n, edges, hasApple))
# Output: 8
# Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.

# #! Example 2:
n = 7
edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
hasApple = [False, False, True, False, False, True, False]
print(minTime(n, edges, hasApple))
# # Output: 6
# # Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.

# #! Example 3:
n = 7
edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
hasApple = [False, False, False, False, False, False, False]
print(minTime(n, edges, hasApple))
# # Output: 0
