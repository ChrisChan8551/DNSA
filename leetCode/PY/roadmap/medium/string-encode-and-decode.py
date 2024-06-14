# https://neetcode.io/problems/string-encode-and-decode

# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode


#! Example 1:
# Input: ["neet","code","love","you"]
# Output:["neet","code","love","you"]

#! Example 2:
# Input: ["we","say",":","yes"]
# Output: ["we","say",":","yes"]
# Constraints:

# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains only UTF-8 characters.

def encode(strs):
    result = ''
    # when you encode a string, there can be non alpha characters. You will need to use some delimiter to separate the words such as #.
    # keep track of length of the string
    # ["neet","code","love","you"] neet -> 4#neet
    result = ''
    for s in strs:
        result += str(len(s)) + '#' + s
    return result


def decode(s):
    result = []
    i = 0
    # use 2 pointer strategy
    while i < len(s):
        # j will represent the last index right before # was found
        j = i
        while s[j] != '#':
            j += 1
        wordlength = int(s[i:j])
        # j will be at the delimiter so add 1.

        result.append(s[j + 1: j + 1 + wordlength])
        # update the i to the next word
        i = j + 1 + wordlength
    return result


#! Example 1:
strs = ["neet", "code", "love", "you"]
print(decode(encode(strs)))
# Output:["neet","code","love","you"]

#! Example 2:
strs = ["we", "say", ":", "yes"]
print(decode(encode(strs)))
# Output: ["we","say",":","yes"]
