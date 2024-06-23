# https://leetcode.com/problems/container-with-most-water/

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.


#! Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

#! Example 2:
# Input: height = [1,1]
# Output: 1


# Constraints:
# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104

#! brute force
# def maxArea(height):
#     # this is a non sorted array or list of numbers
#     # brute force would be to compare all combinations possible to determine max Area.
#     # area is L x H - to get length will need to subtract indexes
#     n = len(height)
#     max_Area = 0
#     for i in range(n):
#         for j in range(i + 1, n):
#             length = j - i
#             current = length * min(height[j], height[i])
#             max_Area = max(max_Area, current)

#     return max_Area

#! 2 pointer
def maxArea(height):
    left, right = 0, len(height) - 1
    max_Area = 0
    while left < right:
        length = right - left
        # you can only use the shorter of the heights to find max Area
        currentHeight = min(height[left], height[right])
        currentArea = length * currentHeight
        max_Area = max(max_Area, currentArea)
        # move the left pointer if the height on the left pointer is less than right to potentially find a larger number. Vice versa decrease the right pointer.
        if (height[left] < height[right]):
            left += 1
        else:
            right -= 1
    return max_Area


#! Example 1:
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

#! Example 2:
height = [1, 1]
print(maxArea(height))
# Output: 1
