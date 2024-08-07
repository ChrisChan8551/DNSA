# https://leetcode.com/problems/detect-squares/

# You are given a stream of points on the X-Y plane. Design an algorithm that:

# Adds new points from the stream into a data structure. Duplicate points are allowed and should be treated as different points.
# Given a query point, counts the number of ways to choose three points from the data structure such that the three points and the query point form an axis-aligned square with positive area.
# An axis-aligned square is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.

# Implement the DetectSquares class:

# DetectSquares() Initializes the object with an empty data structure.
# void add(int[] point) Adds a new point point = [x, y] to the data structure.
# int count(int[] point) Counts the number of ways to form axis-aligned squares with point point = [x, y] as described above.


# Example 1:
# Input
# ["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
# [[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
# Output
# [null, null, null, null, 1, 0, null, 2]

# Explanation
# DetectSquares detectSquares = new DetectSquares();
# detectSquares.add([3, 10]);
# detectSquares.add([11, 2]);
# detectSquares.add([3, 2]);
# detectSquares.count([11, 10]);  return 1. You can choose:
#                                - The first, second, and third points
# detectSquares.count([14, 8]);  // return 0. The query point cannot form a square with any points in the data structure.
# detectSquares.add([11, 2]);    // Adding duplicate points is allowed.
# detectSquares.count([11, 10]); // return 2. You can choose:
#                                   - The first, second, and third points
#

# Constraints:
# point.length == 2
# 0 <= x, y <= 1000
# At most 3000 calls in total will be made to add and count.

# Hint 1
# Maintain the frequency of all the points in a hash map.
# Hint 2
# Traverse the hash map and if any point has the same y-coordinate as the query point, consider this point and the query point to form one of the horizontal lines of the square.

from collections import defaultdict


class DetectSquares:
    # need a way to track points
    # keep track using a hash table (defaultdict(int))
    # keys = tuple(x,y)
    # find diagonal points
    # count point = x1,y1
    # compare point = x2,y2

    # draw lines to see if we can find points in such a way that it can create a square
    # finding points on the same X and Y axis

    def __init__(self):
        self.points = defaultdict(int) # int will default value to zero

    def add(point):
        self.points[tuple(point)] += 1

    def count(point):
        x1, y1 = point
        squares = 0
        for x2, y2 in self.points:
            if abs(x1-x2) == abs(y1-y2):
                corner1 = (x1, y2)
                corner2 = (x2, y1)

            if self.points[corner1] and self.points[corner2]:
                squares += self.points[(x2,y2)] * self.points[corner1] * self.points[corner2]

        return squares


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
