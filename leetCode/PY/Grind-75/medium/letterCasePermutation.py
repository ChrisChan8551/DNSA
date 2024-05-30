# https://leetcode.com/problems/letter-case-permutation/

# Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

# Return a list of all possible strings we could create. Return the output in any order.


#! Example 1:
# Input: s = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]

#! Example 2:
# Input: s = "3z4"
# Output: ["3z4","3Z4"]


# Constraints:

# 1 <= s.length <= 12
# s consists of lowercase English letters, uppercase English letters, and digits.

def letterCasePermutation(s):
    # when looking for all combinations usually means backtracking problem
    # DFS through the decision tree
    # base case when we finish building the string - len(result) = len(s), or i === len(s)
    result = set()

    def _backtrack(i, solution):
        if len(solution) == len(s):
            result.add(solution)
            return
        # decision tree to make character lowercase or uppercase
        # TODO recursion here
        # checking if the character is a number will optimize the solution
        _backtrack(i+1, solution + s[i].lower())
        if not s[i].isnumeric():
            _backtrack(i+1, solution + s[i].upper())
    _backtrack(0, '')
    return list(result)


#! Example 1:
s = "a1b2"
print(letterCasePermutation(s))
# Output: ["a1b2","a1B2","A1b2","A1B2"]

#! Example 2:
s = "3z4"
print(letterCasePermutation(s))
# Output: ["3z4","3Z4"]
