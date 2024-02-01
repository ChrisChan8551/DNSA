# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false


# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

def isValid(s):
    # declare stack array to hold first index
    stack = []
    # create key value pairs in object
    valid = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    # transverse through the string
    for char in s:
        # look if char is one of the valid values, then add into the stack
        if char in valid.values():
            stack.append(char)
        # check the stack if empty or the value inside matches a 'key' in valid object.
        # if it matches then compare the
        elif char in valid.keys():
            if not stack or stack.pop() != valid[char]:
                return False
        else:
            return False
    return not stack


#! TEST_01
s = '()'
# -> True
print(isValid(s))

# #! TEST_02
s = "()[]{}"
# -> True
print(isValid(s))

# #! TEST_03
s = "(]"
# -> False
print(isValid(s))
