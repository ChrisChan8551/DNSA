# Write a function, most_frequent_char, that takes in a string as an argument. The function should return the most frequent character of the string. If there are ties, return the character that appears earlier in the string.

# You can assume that the input string is non-empty.

def most_frequent_char(s):
    count = {}
    for char in s:
        if char not in count:
            count[char] = 0
        count[char] += 1

    most_freq = None
    for char in s:
        if most_freq is None or count[char] > count[most_freq]:
            most_freq = char
    return most_freq


##!TEST_00
print(most_frequent_char('bookeeper'))  # -> 'e'

##!TEST_00
print(most_frequent_char('david'))  # -> 'd'

##!TEST_00
print(most_frequent_char('abby'))  # -> 'b'

##!TEST_00
print(most_frequent_char('mississippi'))  # -> 'i'

##!TEST_00
print(most_frequent_char('potato'))  # -> 'o'

##!TEST_00
print(most_frequent_char('eleventennine'))  # -> 'e'

##!TEST_00
print(most_frequent_char('riverbed'))  # -> 'r'
