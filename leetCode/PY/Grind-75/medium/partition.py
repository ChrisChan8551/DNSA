# https://leetcode.com/problems/palindrome-partitioning/

# Given a string s, partition s such that every
# substring
#  of the partition is a
# palindrome
# . Return all possible palindrome partitioning of s.


#! Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]

#! Example 2:
# Input: s = "a"
# Output: [["a"]]


# Constraints:
# 1 <= s.length <= 16
# s contains only lowercase English letters.


# def partition(s):
#     # initialize results array
#     # create palindrome helper checker (sequence that reads same forward and backward)
#     # create recursive backtracking function
#     # check every combination (partition). If partition is a palindrome, keep traversing path.
#     # base case
#     # when partition reaches end of string or end of the tree
#     # when this is complete and we have a valid solution, add it to the results array.
#     result = []

#     def _palindrome(s):
#         # using 2 pointer is faster than using 'return s == s[::-1]
#         # create 2 pointers left, right
#         left, right = 0, len(s) - 1
#         while left < right:
#             if s[left] != s[right]:
#                 return False
#             left += 1
#             right -= 1
#         return True

#     # i is index of string of last cut of partition, 2nd argument will be the solutions array being returned.
#     def _backtrack(i, solution):
#         # check while index has not reached end of string
#         if i == len(s):
#             # once we reach the end, we append a copy of the solution array. If you don't make a copy, it'll show up as empty arrays.
#             result.append(solution.copy())
#             return  # exit the function

#         for j in range(i, len(s)):
#             substring = s[i:j+1]
#             # check substrings if they are palindromes
#             if _palindrome(substring):
#                 # call backtrack function where j + 1 is the index of substring, and concat solution array with substring array
#                 _backtrack(j + 1, solution + [substring])

#     # start at 0 index, and also start with empty solutions array
#     _backtrack(0, [])
#     return result


#! faster on leetcode
def partition(s):
    def is_palindrome(sub):
        return sub == sub[::-1]

    def backtrack(start, path):
        if start == len(s):
            partitions.append(path[:])
            return

        for end in range(start + 1, len(s) + 1):
            if is_palindrome(s[start:end]):
                path.append(s[start:end])
                backtrack(end, path)
                path.pop()

    partitions = []
    backtrack(0, [])
    return partitions

#! Example 1:
s = "aab"
print(partition(s))
# Output: [["a","a","b"],["aa","b"]]

#! Example 2:
s = "a"
print(partition(s))
# Output: [["a"]]
