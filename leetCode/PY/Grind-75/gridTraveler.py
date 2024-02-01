
# #! brute force
# def gridTraveler(m, n):
#     # base cases
#     if (m == 1 and n == 1):
#         return 1
#     if (m == 0 or n == 0):
#         return 0
#     #moving downward(m-1), and moving right (n-1)
#     return gridTraveler(m-1, n) + gridTraveler(m, n-1)

#! memoization
def gridTraveler(m, n, memo={}):
    # memo base case
    key = (m, n) # coordinates in grid

    if key in memo:
        return memo[key]

    # base cases
    if (m == 1 and n == 1):
        return 1
    if (m == 0 or n == 0):
        return 0
    # moving downward(m-1), and moving right (n-1)
    memo[key] = gridTraveler(m-1, n, memo) + gridTraveler(m, n-1, memo)
    return memo[key]


print(gridTraveler(1, 1))  # -> 1
print(gridTraveler(2, 3))  # -> 3
print(gridTraveler(3, 2))  # -> 3
print(gridTraveler(3, 3))  # -> 6
print(gridTraveler(18, 18))  # -> 2333606220
print(gridTraveler(100, 100))  # -> 22750883079422934966181954039568885395604168260154104734000
