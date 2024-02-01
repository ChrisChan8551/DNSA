# Write a function, can_concat, that takes in a string and a list of words as arguments. The function should return boolean indicating whether or not it is possible to concatenate words of the list together to form the string.

# You may reuse words of the list as many times as needed.
import timeit
start_time = timeit.default_timer()

# #! Brute force
# def can_concat(s, words):
#     if s == '':
#         return True
#     for word in words:
#         if word in s and s.index(word) == 0:
#             suffix = s[len(word):]
#             if (can_concat(suffix, words) == True):
#                 return True
#     return False

#! memoization


def can_concat(s, words, memo={}):
    if s in memo:
        return memo[s]
    if s == '':
        return True
    for word in words:
        if word in s and s.index(word) == 0:
            suffix = s[len(word):]
            if (can_concat(suffix, words, memo) == True):
                memo[s] = True
                return True
    memo[s] = False
    return False


#! TEST_00
print(can_concat("oneisnone", ["one", "none", "is"]))  # -> True

#! TEST_01
print(can_concat("oneisnone", ["on", "e", "is"]))  # -> False

#! TEST_02
print(can_concat("oneisnone", ["on", "e", "is", "n"]))  # -> True

#! TEST_03
print(can_concat("foodisgood", ["is", "g", "ood", "f"]))  # -> True

#! TEST_04
print(can_concat("santahat", ["santah", "hat"]))  # -> False

#! TEST_05
print(can_concat("santahat", ["santah", "san", "hat", "tahat"]))  # -> True

#! TEST_06
print(can_concat("rrrrrrrrrrrrrrrrrrrrrrrrrrx", [
    "r", "rr", "rrr", "rrrr", "rrrrr", "rrrrrr"]))  # -> False

#! TEST_07
print(can_concat("fooisgood", ["foo", "is", "g", "ood", "f"]))  # -> True


