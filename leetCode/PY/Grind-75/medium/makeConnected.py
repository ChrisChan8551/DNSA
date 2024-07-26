# https://leetcode.com/problems/number-of-operations-to-make-network-connected/


# There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

# You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

# Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.


#! Example 1:
# Input: n = 4, connections = [[0,1],[0,2],[1,2]]
# Output: 1
# Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.

#! Example 2:
# Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
# Output: 2

#! Example 3:
# Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
# Output: -1
# Explanation: There are not enough cables.


# Constraints:

# 1 <= n <= 105
# 1 <= connections.length <= min(n * (n - 1) / 2, 105)
# connections[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# There are no repeated connections.
# No two computers are connected by more than one cable.

# Hint 1
# As long as there are at least (n - 1) connections, there is definitely a way to connect all computers.
# Hint 2
# Use DFS to determine the number of isolated computer clusters.


from collections import defaultdict


def makeConnected(n, connections):
    # undirected graph problem
    # model as an undirected graph using adjacency list
    # minimum number of cables to connect all computers must be 1 less than total number of computers (n - 1)
    # number of connections that need to be moved are equivalent to number of connected groups minus 1.
    # use DFS to determine how many clusters we have
    # similar problem is  https://leetcode.com/problems/number-of-islands/
    num_clusters = 0
    visited = set()

    def _dfs(node):
        if node in visited:
            return 0

        visited.add(node)
        for neighbor in graph[node]:
            _dfs(neighbor)

        return 1

    if len(connections) < n - 1:
        return - 1

    graph = defaultdict(list)
    for a, b in connections:
        graph[a].append(b)
        graph[b].append(a)

    for node in range(n):
        num_clusters += _dfs(node)

    # print(graph)


    return num_clusters - 1


#! Example 1:
n = 4
connections = [
    [0, 1],
    [0, 2],
    [1, 2]
]
# 0 : { 1, 2 }
# 1 : { 2 }
print(makeConnected(n, connections))
# Output: 1
# Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.

#! Example 2:
n = 6
connections = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]
print(makeConnected(n, connections))
# Output: 2

#! Example 3:
n = 6
connections = [[0, 1], [0, 2], [0, 3], [1, 2]]
print(makeConnected(n, connections))
# Output: -1
# Explanation: There are not enough cables.
