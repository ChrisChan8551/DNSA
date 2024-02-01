# Write a function, anagrams, that takes in two strings as arguments. The function should return a boolean indicating whether or not the strings are anagrams. Anagrams are strings that contain the same characters, but in any order.

#! Easy way
def anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

#! using dictionaries
# def anagrams(s1, s2):
#   return char_count(s1) == char_count(s2)

# def char_count(s):
#   count = {}

#   for char in s:
#     if char not in count:
#       count[char] = 0
#     count[char] += 1


#   return count
#! using Counters

# from collections import Counter
# def anagrams(s1, s2):
#     return Counter(s1) == Counter(s2)


# !TEST_00
print(anagrams('restful', 'fluster'))  # -> True
# !TEST_01
print(anagrams('cats', 'tocs'))  # -> False
# !TEST_02
print(anagrams('monkeyswrite', 'newyorktimes'))  # -> True
# !TEST_03
print(anagrams('paper', 'reapa'))  # -> False
# !TEST_04
print(anagrams('elbow', 'below'))  # -> True
# !TEST_05
print(anagrams('tax', 'taxi'))  # -> False
# !TEST_06
print(anagrams('taxi', 'tax'))  # -> False
# !TEST_07
print(anagrams('night', 'thing'))  # -> True
# !TEST_08
print(anagrams('abbc', 'aabc'))  # -> False
# !TEST_09
print(anagrams('po', 'popp'))  # -> false
# !TEST_10
print(anagrams('pp', 'oo'))  # -> false
