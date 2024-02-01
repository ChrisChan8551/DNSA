# Write a function, quickest_concat, that takes in a string and a list of words as arguments. The function should return the minimum number of words needed to build the string by concatenating words of the list.

# You may use words of the list as many times as needed.
import timeit
start_time = timeit.default_timer()

#! Brute Force
# def quickest_concat(s, words):
#     if s == '':
#         return 1
#     totalCount = 0

#     for word in words:
#         if word in s and s.index(word) == 0:
#             # if s.index(word) == 0:

#             numWaysForRest = quickest_concat(s[len(word):], words)
#             totalCount += numWaysForRest

#     return totalCount

#! Memoization


def quickest_concat(s, words, memo={}):
    if s in memo:
        return memo[s]
    if s == '':
        return 1
    totalCount = 0

    for word in words:
        if word in s and s.index(word) == 0:
            # if s.index(word) == 0:

            numWaysForRest = quickest_concat(s[len(word):], words, memo)
            totalCount += numWaysForRest
    memo[s] = totalCount
    return totalCount


#! TEST_00
print(quickest_concat('caution', ['ca', 'ion', 'caut', 'ut']))  # -> 2

#! TEST_01
print(quickest_concat('caution', ['ion', 'caut', 'caution']))  # -> 1

#! TEST_02
print(quickest_concat('respondorreact', [
    're', 'or', 'spond', 'act', 'respond']))  # -> 4

#! TEST_03
print(quickest_concat('simchacindy', [
      'sim', 'simcha', 'acindy', 'ch']))  # -> 3

#! TEST_04
print(quickest_concat('simchacindy', ['sim', 'simcha', 'acindy']))  # -> -1

#! TEST_05
print(quickest_concat('uuuuuu', ['u', 'uu', 'uuu', 'uuuu']))  # -> 2

#! TEST_06
print(quickest_concat('rongbetty', ['wrong', 'bet']))  # -> -1

#! TEST_07
print(quickest_concat('uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu', [
    'u', 'uu', 'uuu', 'uuuu', 'uuuuu']))  # -> 7


# print(quickest_concat('purple', ['purp', 'p', 'ur', 'le', 'purpl'])) #2
# print(quickest_concat('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])) #1
# print(quickest_concat('skateboard', [
#       'bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar' 'purpl'])) #0
# print(quickest_concat('enterpotentpot', [
#       'a', 'p', 'ent', 'enter', 'ot', 'o', 't'])) #4
# print(quickest_concat('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeeee', 'eeeeee'])) # 0
