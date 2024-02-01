# Write a function, compress, that takes in a string as an argument. The function should return a compressed version of the string where consecutive occurrences of the same characters are compressed into the number of occurrences followed by the character. Single character occurrences should not be changed.

# 'aaa' compresses to '3a'
# 'cc' compresses to '2c'
# 't' should remain as 't'
# You can assume that the input only contains alphabetic characters.

def compress(s):
    s+='!' # in python you need to add a 'place holder' to the end of the string.
    result = []
    i = 0
    j = 0
    # need to have 2 pointers. 1 for the initial letter, and how many characters after the initial letter

    while (j < len(s)):
        # if pointers match 2nd pointer +1
        if (s[i] == s[j]):
            j += 1
        else:
            # if the pointers go to a different character then subject the difference between the 2 points to get the count of characters
            count = j - i
        # if there is only 1 letter, then push the single letter into the result
        if (count == 1):
            result.append(s[i])
        # else push the number and the letter into the result array
        else:
            # number needs to be converted into a string push into result, then push letter into the result array
            result.append(str(count))
            result.append(s[i])
        # set i to j because it's the next character.
        # return join array
    return ''.join(result)

#! alternate implementation
def compress(s):
    result = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i+1]:
            count += 1
            i += 1
        if count > 1:
            result.append(str(count) + s[i])
        else:
            result.append(s[i])
        i += 1
    return ''.join(result)

# loop through the string


#! TEST_00
print(compress('ccaaatsss'))  # -> '2c3at3s'

#! TEST_01
print(compress('ssssbbz'))  # -> '4s2bz'

#! TEST_02
print(compress('ppoppppp'))  # -> '2po5p'

#! TEST_03
print(compress('nnneeeeeeeeeeeezz'))  # -> '3n12e2z'

#! TEST_04
print(compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'))
# -> '127y'
