# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


#! Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

#! Example 2:
# Input: digits = ""
# Output: []

#! Example 3:
# Input: digits = "2"
# Output: ["a","b","c"]


# Constraints:
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

def letterCombinations(digits):
    # recursion solution - DFS
    # setup a dictionary for all the letters associated with each number on the phone.
    # base case if digits is blank return empty array []
    if not digits:
        return []

    keyboard = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

    # declaring DFS function accepting an index and path as arguments
    def _DFS(index, path):
        # base case - once index reaches length of digits array, recursive function is complete
        if index == len(digits):
            combo.append(''.join(path))
            return
        # loop through digits at index X, add it to path
        for char in keyboard[digits[index]]:
            path.append(char)
            _DFS(index + 1, path)
            path.pop()

    # declaring variable to hold all combinations of letters
    combo = []
    # recalling recursive function
    _DFS(0, [])
    return combo


#! Example 1:
digits = "23"
print(letterCombinations(digits))
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

#! Example 2:
digits = ""
print(letterCombinations(digits))
# Output: []

#! Example 3:
digits = "2"
print(letterCombinations(digits))
# Output: ["a","b","c"]
