# Write a function, largest_component, that takes in the adjacency list of an undirected graph. The function should return the size of the largest connected component in the graph.
from collections import deque

#! my way breadth


def largest_component(graph):
    visited = set()
    largest_component = 0

    for node in graph:
        print('node :', node)

        if node not in visited:
            count = 0
            queue = deque([node])
            while queue:
                current = queue.popleft()
                print('current: ', current)
                if current not in visited:
                    visited.add(current)
                    count += 1
                    for neighbor in graph[current]:
                        if neighbor not in visited:
                            queue.append(neighbor)
            if count > largest_component:
                largest_component = count
    return largest_component


#! TEST_00
print(largest_component({
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}))  # -> 4

#! TEST_01
print(largest_component({
    1: [2],
    2: [1, 8],
    6: [7],
    9: [8],
    7: [6, 8],
    8: [9, 7, 2]
}))  # -> 6

#! TEST_02
print(largest_component({
    3: [],
    4: [6],
    6: [4, 5, 7, 8],
    8: [6],
    7: [6],
    5: [6],
    1: [2],
    2: [1]
}))  # -> 5

#! TEST_03
print(largest_component({}))  # -> 0

#! TEST_04
print(largest_component({
    0: [4, 7],
    1: [],
    2: [],
    3: [6],
    4: [0],
    6: [3],
    7: [0],
    8: []
}))  # -> 3
