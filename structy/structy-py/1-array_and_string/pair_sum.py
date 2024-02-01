# Write a function, pair_sum, that takes in a list and a target sum as arguments. The function should return a tuple containing a pair of indices whose elements sum to the given target. The indices returned must be unique.

# Be sure to return the indices, not the elements themselves.

# There is guaranteed to be one such pair that sums to the target.

##! Brute force
# def pair_sum(numbers, target_sum):
#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             if numbers[i]+numbers[j] == target_sum:
#                 return (i, j)
#
##! Best time complexity
def pair_sum(numbers, target_sum):
    # Create a dictionary to store the value-index pairs
    pairs = {}

    for idx, num in enumerate(numbers):
        # Calculate the complement needed to reach the target
        complement = target_sum - num

        # Check if the complement exists in the dictionary
        if complement in pairs:
            # Return the indices of the current number and its complement
            return (pairs[complement], idx)
        pairs[num] = idx
    # This return statement should not be reached if there is always a valid pair
    return None


# ##! TEST_00
print(pair_sum([3, 2, 5, 4, 1], 8))  # -> (0, 2)

# ##! TEST_01
# print(pair_sum([4, 7, 9, 2, 5, 1], 5)) # -> (0, 5)

# ##! TEST_02
# print(pair_sum([4, 7, 9, 2, 5, 1], 3)) # -> (3, 5)

# ##! TEST_03
# print(pair_sum([1, 6, 7, 2], 13)) # -> (1, 2)

# ##! TEST_04
# print(pair_sum([9, 9], 18)) # -> (0, 1)

# ##! TEST_05
# print(pair_sum([6, 4, 2, 8 ], 12)) # -> (1, 3)
