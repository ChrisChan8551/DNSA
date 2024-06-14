# https://leetcode.com/problems/valid-parentheses/

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

#! Example 1:
# Input: s = "()"
# Output: true

#! Example 2:
# Input: s = "()[]{}"
# Output: true

#! Example 3:
# Input: s = "(]"
# Output: false


# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.


def isValid(s):
    stack = []
    valid = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    if len(s) % 2 == 1:
        return False
    for char in s:
        if char in valid:
            if stack and stack[-1] == valid[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return len(stack) == 0


#! Example 1:
s = "()"
print(isValid(s))
# Output: true

#! Example 2:
s = "()[]{}"
print(isValid(s))
# Output: true

#! Example 3:
s = "(]"
print(isValid(s))
# Output: false

#! Example 4:
s = "([{}])"
print(isValid(s))
# Output: true
