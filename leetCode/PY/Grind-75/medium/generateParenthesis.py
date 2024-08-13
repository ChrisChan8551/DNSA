# https://leetcode.com/problems/generate-parentheses/


# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


#! Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

#! Example 2:
# Input: n = 1
# Output: ["()"]


# Constraints:

# 1 <= n <= 8

def generateParenthesis(n):
    #! key phrase 'all combinations' means backtracking problem or recursive.
    def _dfs(s, left, right):
        # base case. The length of the final string should be 2 x n length.
        if len(s) == n * 2:
            res.append(s)
            return
        # keeps adding the left parenthesis until it hits n times.
        if left < n:
            _dfs(s + '(', left + 1, right)
        # keeps adding the right parenthesis until it hits left times
        if right < left:
            _dfs(s + ')', left, right + 1)

    res = []
    #begin with empty string, start at 0 parenthesis left and right
    _dfs('', 0, 0)
    return res


#! Example 1:
n = 3
print(generateParenthesis(n))
# Output: ["((()))","(()())","(())()","()(())","()()()"]

#! Example 2:
n = 1
print(generateParenthesis(n))
# Output: ["()"]
