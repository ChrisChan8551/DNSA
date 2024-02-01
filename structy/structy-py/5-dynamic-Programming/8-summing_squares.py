# Write a function, summing_squares, that takes a target number as an argument. The function should return the minimum number of perfect squares that sum to the target. A perfect square is a number of the form (i*i) where i >= 1.

# For example: 1, 4, 9, 16 are perfect squares, but 8 is not perfect square.

# Given 12:

# summing_squares(12) -> 3

# The minimum squares required for 12 is three, by doing 4 + 4 + 4.

# Another way to make 12 is 9 + 1 + 1 + 1, but that requires four perfect squares.


def summing_squares(n):
  pass # todo

#! TEST_00
summing_squares(8) # -> 2

#! TEST_01
summing_squares(9) # -> 1

#! TEST_02
summing_squares(12) # -> 3

#! TEST_03
summing_squares(1) # -> 1

#! TEST_04
summing_squares(31) # -> 4

#! TEST_05
summing_squares(50) # -> 2

#! TEST_06
summing_squares(68) # -> 2

#! TEST_07
summing_squares(87) # -> 4
