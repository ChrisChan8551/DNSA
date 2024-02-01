# https://leetcode.com/problems/search-a-2d-matrix/

# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.


# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false


# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104

# #! brute force
# def searchMatrix(matrix, target):
#     rows, cols = len(matrix), len(matrix[0])

#     for i in range(rows):
#         for j in range(cols):
#             if matrix[i][j] == target:
#                 return True

#     return False

#! 0(log m x n)
# def searchMatrix(matrix, target):
#     # you can binary search by row and col
#     rows = len(matrix)
#     cols = len(matrix[0])
#     top = 0
#     bottom = rows-1
#     while top <= bottom:
#         row = top + (bottom - top) // 2
#         if target > matrix[row][cols - 1]:
#             top += 1
#         elif target < matrix[row][0]:
#             bottom -= 1
#         else:
#             break

#     if top > bottom:
#         return False

#     row = top + (bottom - top) // 2
#     left, right = 0, cols-1

#     while left <= right:
#         mid = left + (right - left)//2
#         if target > matrix[row][mid]:
#             left = mid + 1
#         elif target < matrix[row][mid]:
#             right = mid-1
#         else:
#             return True
#     return False

def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1

    while left <= right:
        mid = left + (right - left) // 2
        mid_element = matrix[mid // cols][mid % cols]

        if mid_element == target:
            return True
        elif mid_element < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
# Output: true

print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
# Output: false
