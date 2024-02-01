# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.


# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1


# Constraints:

# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104


#! O(n^2)
# def maxArea(height):
#     maxArea = 0
#     for i in range(len(height)):
#         for j in range(i+1, len(height)):
#             currentArea = (j-i) * min(height[j], height[i])
#             if currentArea > maxArea:
#                 maxArea = currentArea
#     return maxArea

#! O(n)
def maxArea(height):
    # 2 pointer method setting left, and right at the end of the container
    # set maxArea variable to keep track
    left = 0
    right = len(height)-1
    maxArea = 0
    # set while loop as long as left is less than right.
    while (left < right):
        # to get area between left and right, calculate the minimum between the 2, and multiply by the distance of the 2 columns (right-left)
        currentArea = min(height[left], height[right]) * (right-left)
        # set maxArea to greater Area
        maxArea = max(maxArea, currentArea)
        if (height[left] < height[right]):
            # increase left to move to center of the graph
            left += 1
        else:
            # decrease right to move to center of the graph
            right -= 1
    return maxArea


print(maxArea([1, 1]))  # -> 1
print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # -> 49

