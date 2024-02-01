# Start with an initial string of zeros. Choose any digit to flip. When a digit is flipped, its value and
# those to the right switch state between 0 and 1. Given a target string of binary digits, determine
# the minimum number of flips required to achieve the target.
# Example:
# target = 01011
# Start with a string of 5 zeros, the same length st ring as the target.
# Initial String -> 00000
# Flip the 3rd digit -> 00111
# Flip the 2nd digit -> 01000
# Flip the 4th digit -> 01011
# 3 flips are required to reach the target. The return value is 3.
# Function Description
# Complete the function minimum flips in the editor below.
# minimumF/ips has the following parameter(s):
# string target: a string of Os and 1s to match
# Returns:
# int: the minimum number of flips needed to obtain the target string
# Constraints
# • 1 :s length of target :s 1 a5
# • O :5 target[i] :5 1
# • The target string consists of digits O and 1


# def minimumFlips(target):
#     flips = 0
#     current_state = '0' * len(target)

#     for i in range(len(target)):
#         if target[i] != current_state[i]:
#             flips += 1
#             current_state = current_state[:i] + target[i] * (len(target) - i)

#     return flips

def minimumFlips(target):
    flips = 0
    status = '0'
    for current in target:
        if current != status:
            flips += 1
            status = '0' if status == '1' else '1'
    return flips


# Example usage:
target = "01011"
result = minimumFlips(target)
print(result)

target = "0011"
result = minimumFlips(target)
print(result)

target = "1010"
result = minimumFlips(target)
print(result)
