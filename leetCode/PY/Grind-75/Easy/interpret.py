# https://leetcode.com/problems/goal-parser-interpretation/

# You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

# Given the string command, return the Goal Parser's interpretation of command.


#! Example 1:
# Input: command = "G()(al)"
# Output: "Goal"
# Explanation: The Goal Parser interprets the command as follows:
# G -> G
# () -> o
# (al) -> al
# The final concatenated result is "Goal".

#! Example 2:
# Input: command = "G()()()()(al)"
# Output: "Gooooal"

#! Example 3:
# Input: command = "(al)G(al)()()G"
# Output: "alGalooG"


# Constraints:

# 1 <= command.length <= 100
# command consists of "G", "()", and/or "(al)" in some order.

# Hint 1
# You need to check at most 2 characters to determine which character comes next.

# def interpret(command):
#     result = ''
#     for i in range(len(command)):
#         if command[i] == 'G':
#             result += "G"
#         elif command[i] == '(' and command[i+1] == ')':
#             result += 'o'
#         elif command[i] == '(' and command[i+1] == 'a':
#             result += 'al'
#     return result


def interpret(command):
    return command.replace("()", "o").replace("(al)", "al")


#! Example 1:
command = "G()(al)"
print(interpret(command))
# Output: "Goal"
# Explanation: The Goal Parser interprets the command as follows:
# G -> G
# () -> o
# (al) -> al
# The final concatenated result is "Goal".

#! Example 2:
command = "G()()()()(al)"
print(interpret(command))
# Output: "Gooooal"

#! Example 3:
command = "(al)G(al)()()G"
print(interpret(command))
# Output: "alGalooG"
