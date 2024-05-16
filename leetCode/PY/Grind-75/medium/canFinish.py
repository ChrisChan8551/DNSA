# https://leetcode.com/problems/course-schedule/

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.


#! Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.

#! Example 2:
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.


# Constraints:

# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.


from collections import defaultdict


#! graph problem, high frequency asked problem.
def canFinish(numCourses, prerequisites):
    # cycle detection problem.
    # prerequisites are essentially edges in an a directed path
    # need a starting point to take every course
    # model graph using adjacency list
    #! this requires recursion using DFS or BFS
    # [[0,1][0,2][1,3],[1,4],[3,4]]
    # 0 -> 1
    # 0 -> 2
    # 1 -> 3
    # 1 -> 4
    # 3 -> 4
    #! base case - if course has no neighbors / prerequisites then it's a valid starting point
    adj_list = defaultdict(list)
    for course, prereq in prerequisites:
        adj_list[course].append(prereq)

    validated = set()

    def _hasCycle(course, visited):
        # success base case
        if len(adj_list[course]) == 0:
            return False

        # failed base case = if there is a cycle of courses
        if course in visited:
            return True

        visited.add(course)

        for prereq in adj_list[course]:
            if course not in validated and _hasCycle(prereq, visited):
                return True
        visited.remove(course)
        validated.add(course)

    for course in range(numCourses):
        if _hasCycle(course, set()):
            return False

    return True


#! Example 1:
numCourses = 2
prerequisites = [[1, 0]]
print(canFinish(numCourses, prerequisites))
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.

#! Example 2:
numCourses = 2
prerequisites = [[1, 0], [0, 1]]
print(canFinish(numCourses, prerequisites))
# Output: false
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

#! Example 3:
numCourses = 2
prerequisites = [[1, 0]]
print(canFinish(numCourses, prerequisites))
# Output: true

#! Example 4:
numCourses = 8
prerequisites = [[1, 0], [2, 6], [1, 7], [6, 4], [7, 0], [0, 5]]
print(canFinish(numCourses, prerequisites))
# Output: true
