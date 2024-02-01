# Write a function, prereqs_possible, that takes in a number of courses (n) and prerequisites as arguments. Courses have ids ranging from 0 through n - 1. A single prerequisite of (A, B) means that course A must be taken before course B. The function should return a boolean indicating whether or not it is possible to complete all courses.

def prereqs_possible(num_courses, prereqs):
  pass # todo

#! TEST_00
numCourses = 6
prereqs = [
  (0, 1),
  (2, 3),
  (0, 2),
  (1, 3),
  (4, 5),
]
prereqs_possible(numCourses, prereqs) # -> True

#! TEST_01
numCourses = 6
prereqs = [
  (0, 1),
  (2, 3),
  (0, 2),
  (1, 3),
  (4, 5),
  (3, 0),
]
prereqs_possible(numCourses, prereqs) # -> False

#! TEST_02
numCourses = 5
prereqs = [
  (2, 4),
  (1, 0),
  (0, 2),
  (0, 4),
]
prereqs_possible(numCourses, prereqs) # -> True

#! TEST_03
numCourses = 6
prereqs = [
  (2, 4),
  (1, 0),
  (0, 2),
  (0, 4),
  (5, 3),
  (3, 5),
]
prereqs_possible(numCourses, prereqs) # -> False

#! TEST_04
numCourses = 8
prereqs = [
  (1, 0),
  (0, 6),
  (2, 0),
  (0, 5),
  (3, 7),
  (4, 3),
]
prereqs_possible(numCourses, prereqs) # -> True

#! TEST_05
numCourses = 8
prereqs = [
  (1, 0),
  (0, 6),
  (2, 0),
  (0, 5),
  (3, 7),
  (7, 4),
  (4, 3),
]
prereqs_possible(numCourses, prereqs) # -> False

#! TEST_06
numCourses = 42
prereqs = [(6, 36)]
prereqs_possible(numCourses, prereqs) # -> True
