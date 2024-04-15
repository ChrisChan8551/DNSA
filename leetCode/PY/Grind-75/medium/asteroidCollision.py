# https://leetcode.com/problems/asteroid-collision/

# We are given an array asteroids of integers representing asteroids in a row.

# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.


#! Example 1:
# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

#! Example 2:
# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.

#! Example 3:
# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.


# Constraints:

# 2 <= asteroids.length <= 104
# -1000 <= asteroids[i] <= 1000
# asteroids[i] != 0

# def asteroidCollision(asteroids):
#     # 5 - > stack
#     # 10 pos - > stack
#     # -5 & 10
#     stack = []
#     for asteroid in asteroids:
#         if not stack or asteroid > 0:
#             stack.append(asteroid)
#         else:
#             while True:
#                 if stack[-1] < 0:
#                     stack.append(asteroid)
#                     break
#                 elif stack[-1] == -asteroid:
#                     stack.pop()
#                     break
#                 elif stack[-1] > -asteroid:
#                     break
#                 else:
#                     stack.pop()
#                     if not stack:
#                         stack.append(asteroid)
#                         break
#     return stack

def asteroidCollision(asteroids):
    # 5 - > stack
    # 10 pos - > stack
    # -5 & 10
    stack = []
    for asteroid in asteroids:
        flag = True
        while stack and asteroid < 0 and stack[-1] > 0:
            if abs(asteroid) > stack[-1]:
                stack.pop()
            elif abs(asteroid) == stack[-1]:
                stack.pop()
                flag = False
                break
            else:
                flag = False
        if flag:
            stack.append(asteroid)
    return stack


#! Example 1:
asteroids = [5, 10, -5]
print(asteroidCollision(asteroids))
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

# #! Example 2:
# asteroids = [8,-8]
# print(asteroidCollision(asteroids))
# # Output: []
# # Explanation: The 8 and -8 collide exploding each other.

# #! Example 3:
# asteroids = [10,2,-5]
# print(asteroidCollision(asteroids))
# # Output: [10]
# # Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
