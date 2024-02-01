# Write a function, semesters_required, that takes in a number of courses (n) and a list of prerequisites as arguments. Courses have ids ranging from 0 through n - 1. A single prerequisite of (A, B) means that course A must be taken before course B. Return the minimum number of semesters required to complete all n courses. There is no limit on how many courses you can take in a single semester, as long the prerequisites of a course are satisfied before taking it.

# Note that given prerequisite (A, B), you cannot take course A and course B concurrently in the same semester. You must take A in some semester before B.

# You can assume that it is possible to eventually complete all courses.

#! Structy solution
def semesters_required(num_courses, prereqs):
    # convert prereqs to adjacency list
    # longest path algorithm
    # then look for the terminal nodes, terminal nodes get a distance of 1
    # traverse through the graph depth first
    distance = {}
    # 1) build out graph for the prerequisites using a helper function.
    graph = build_graph(num_courses, prereqs)
    # 6) find the terminal nodes that have no neighbors
    for course in graph:
        if len(graph[course]) == 0:  # when you find the terminal node you set the end to 1
            # this time is 1 because it doesn't make sense to have 0 semesters
            distance[course] = 1
    # 7) initate DFS with the courses
    for course in graph:
        # this will not tell you course in sequence, you only need the longest sequence.
        traverse_distance(graph, course, distance)
        # 11) when you finish you should have a filled distance dictionary. keys to represent nodes, and value on how far they are
    # if you have a dictionary and you use .values(), you're going to get interator of all the values.
    # find the max of the values using max method
    return max(distance.values())

# 2)


def build_graph(num_courses, prereqs):
    graph = {}
    # 3) if a course is 6, then you would need number of courses 1 to 5. That prompts to do a for loop from 0 to num_courses
    for course in range(0, num_courses):  # starting from 0 but not including num_courses
        graph[course] = []  # every course number initalize it as a empty list
    # 4) go through every prereqs
    for prereq in prereqs:
        # 5) deconstruct a,b from prereq
        a, b = prereq
        # because you need a prereq for a course, you will not make a symetric graph. IE you dont need graph[b].append(a)
        graph[a].append(b)
    return graph

# 8) helper function traverse distance


def traverse_distance(graph, node, distance):
    # base case to check if you visited the node
    if node in distance:
        return distance[node]

    # iterate through the neighbors of current node
    # 9)
    max_distance = 0
    for neighbor in graph[node]:
        # recursive call. this will give you a number the longest path that begins at neighbor
        neighbor_distance = traverse_distance(graph, neighbor, distance)
        # 10) track max distance
        if neighbor_distance > max_distance:
            max_distance = neighbor_distance
    distance[node] = max_distance + 1  # store the distance into the node
    return distance[node]


#! alternative
# We start by defining a function called semesters_required that takes two inputs:
# num_courses (the number of courses) and 'prerequisites' (a list describing which courses need to be taken before others).
def semesters_required(num_courses, prerequisites):

    # We create a list called 'in_degree' to keep track of how many prerequisites each course has.
    in_degree = [0] * num_courses
    print(in_degree)
    # We also create a dictionary called 'graph' to represent the relationships between courses and their prerequisites.
    # This dictionary will help us build a map of which course needs to be taken before another.

    graph = {}
    for i in range(num_courses):
        graph[i] = []
    print('graph :', graph)
    #! graph = {i: [] for i in range(num_courses)}

    # Next, we go through the 'prerequisites' list and update 'in_degree' and 'graph' accordingly.
    for course, prereq in prerequisites:
        # For each pair in 'prerequisites', we increase the count of prerequisites for the 'course' by 1.
        in_degree[course] += 1
        # We also add this 'course' as a requirement for the 'prereq' course in our 'graph' dictionary.
        graph[prereq].append(course)
    print('graph :', graph)
    # Now, we create a list called 'queue' to help us perform a special kind of sorting called topological sorting.
    queue = []

    # We start by adding courses that have no prerequisites (in-degree equals 0) to our 'queue'.
    for i in range(num_courses):
        if in_degree[i] == 0:
            queue.append(i)
    print('queue :', queue)
    # We're going to keep track of the number of semesters required to complete the courses.
    semesters = 0

    # Now, we get into the core of our algorithm, which is called topological sorting.
    # We repeat the following steps until our 'queue' is empty.
    while queue:
        # We keep track of the number of courses we can take in this semester.
        num_courses_in_semester = len(queue)
        print('num_courses_in_semester :', num_courses_in_semester)
        # We take all the courses in this semester.
        for _ in range(num_courses_in_semester):
            # We take the next course from the 'queue'.
            course = queue.pop(0)
            print('course :', course)
            # For this course, we decrease the count of prerequisites for the courses that require it.
            for prereq_course in graph[course]:
                in_degree[prereq_course] -= 1

                # If a course no longer has any prerequisites, we add it to the 'queue' for the next semester.
                if in_degree[prereq_course] == 0:
                    queue.append(prereq_course)

        # We've completed a semester, so we increase our 'semesters' count.
        semesters += 1

    # Finally, we return the total number of semesters required to complete all the courses.
    return semesters


#! TEST_00
num_courses = 6
prereqs = [
    (1, 2),
    (2, 4),
    (3, 5),
    (0, 5),
]

# 1 -> 2 -> 4
# 3 -> 5
# 0 -> 5
print(semesters_required(num_courses, prereqs))  # -> 3

# #! TEST_01
# num_courses = 7
# prereqs = [
#     (4, 3),
#     (3, 2),
#     (2, 1),
#     (1, 0),
#     (5, 2),
#     (5, 6),
# ]

# 4 -> 3 -> 2 -> 1 -> 0
# 5 -> 2
# 5 -> 6
# print(semesters_required(num_courses, prereqs))  # -> 5

# #! TEST_02
# num_courses = 5
# prereqs = [
#     (1, 0),
#     (3, 4),
#     (1, 2),
#     (3, 2),
# ]
# 1 -> 0
# 3 -> 4
# 1 -> 2
# 3 -> 2
# print(semesters_required(num_courses, prereqs))  # -> 2

# #! TEST_03
# num_courses = 12
# prereqs = []
# print(semesters_required(num_courses, prereqs))  # -> 1

# #! TEST_04
# num_courses = 3
# prereqs = [
#     (0, 2),
#     (0, 1),
#     (1, 2),
# ]
# print(semesters_required(num_courses, prereqs))  # -> 3

# #! TEST_05
# num_courses = 6
# prereqs = [
#     (3, 4),
#     (3, 0),
#     (3, 1),
#     (3, 2),
#     (3, 5),
# ]
# print(semesters_required(num_courses, prereqs))  # -> 2
