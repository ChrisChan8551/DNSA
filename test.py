
# Overview: For two strings to be isomorphic, all occurrences of a character in a string A can be replaced with another character to get string B.
# The order of the characters must be preserved. There must be one-to-one mapping for every char of string A to every char of string B.
# paper and title would return true.
# egg and sad would return false.
# dgg and add would return true

#
# P = T
# A = I
# P = T
# E = L
# R = E
#
# E = S
# G = A
# G != D
#
# D = A
# G = D
# G = D
#

def isomorphic(s, t):
    if len(s) != len(t):
        return False
    pairs = {}
    for i in range(len(s)):
        charA = s[i]
        charB = t[i]
        pairs[charA] = charB
        pairs[charB] = charA
        print(pairs)


a = 'paper'
b = 'title'
print(isomorphic(a, b))
# true

# a = 'egg'
# b = 'sad'
# print(isomorphic(a, b))
# # #false

# a = 'dgg'
# b = 'add'
# print(isomorphic(a, b))
# # true
