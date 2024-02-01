# Write a function, pair_product, that takes in a list and a target product as arguments. The function should return a tuple containing a pair of indices whose elements multiply to the given target. The indices returned must be unique.

# Be sure to return the indices, not the elements themselves.

# There is guaranteed to be one such pair whose product is the target.

def pair_product(numbers, target_product):
    pairs = {}
    for idx, num in enumerate(numbers):
        complement = target_product/num

        if complement in pairs:
            return (pairs[complement], idx)
        pairs[num] = idx
    return None


##! TEST_00
print(pair_product([3, 2, 5, 4, 1], 8))  # -> (1, 3)

##! TEST_01
print(pair_product([3, 2, 5, 4, 1], 10))  # -> (1, 2)

##! TEST_02
print(pair_product([4, 7, 9, 2, 5, 1], 5))  # -> (4, 5)

##! TEST_03
print(pair_product([4, 7, 9, 2, 5, 1], 35))  # -> (1, 4)

##! TEST_04
print(pair_product([3, 2, 5, 4, 1], 10))  # -> (1, 2)

##! TEST_05
print(pair_product([4, 6, 8, 2], 16))  # -> (2, 3)
