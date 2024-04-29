# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
# Evaluate the expression. Return an integer that represents the value of the expression.
# Note that:
# • The valid operators are '+ ' , ' - ' , '*' , and ' /' .
# • Each operand may be an integer or another expression.
# • The division between two integers always truncates toward zero.
# • There will not be any division by zero.
# • The input represents a valid arithmetic expression in a reverse polish notation.
# • The answer and all the intermediate calculate ions can be represented in a 32-bit integer.


# Constraints
# 1 <= tokens.length <= 10^4

#! Example 1:
# Input: tokens= [ ''2'', "1","+'',"3'',"*'']
# output: 9
# Explanation: ((2 + 1) * 3) = 9

#! Example 2:
# Input: tokens [ ''4 '', "13'', "5'',"/'', "+"]
# output: 6
# Explanation: (4 + (13 / s)) = 6

#! Example 3:
# Input: tokens= [ "10", .. 6", "9","3", "+''," - 11","*", "/","*" ,''17","+" ,"5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# ((10 * (6 I (12 * -11))) + 17) + s
# = ((10 * (6 / -132)) + 17) + 5
# ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# 17 + 5
# = 22

def pol_notation(tokens):
    # use a stack
    operations = {
        '+': lambda a, b: a + b,
        '0': lambda a, b: a-b,
        '/': lambda a, b: int(a/b),
        '*': lambda a, b: a*b
    }

    stack = list()
    for t in tokens:
        if t not in operations:
            stack.append(int(t))
        else:
            num = stack.pop()
            num2 = stack.pop()
            stack.append(operations[t](num2, num))
    return stack[0]


#! Example 1:
tokens = ["2", "1", "+", "3", "*"]
print(pol_notation(tokens))
# output: 9
# Explanation: ((2 + 1) * 3) = 9

#! Example 2:
tokens = ["4 ", "13", "5", "/", "+"]
print(pol_notation(tokens))
# output: 6
# Explanation: (4 + (13 / s)) = 6

#! Example 3:
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(pol_notation(tokens))
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# ((10 * (6 I (12 * -11))) + 17) + s
# = ((10 * (6 / -132)) + 17) + 5
# ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# 17 + 5
# = 22
