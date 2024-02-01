# 1. Longest Even Length Word
# Consider a string, sentence, of words separated by spaces where each word is a substring consisting of English alphabetic letters only. Find the first word in the sentence that has a length which is both an even number and greater than or equal to the length of any other word of even length in the sentence. If there are multiple words meeting the criteria, return the one which occurs first in the sentence.



# Example

# sentence = "Time to write great code"

# The lengths of the words are 4, 2, 5, 5, 4, in order. The longest even length words are Time and code. The one that occurs first is Time, the answer to return



# Function Description

# Complete the function longestEvenWord in the editor below.



# longestEvenWord has the following parameter(s):

    # string sentence:  a sentence string



# Returns:

    # string: the word that is first occurrence of a string with maximal even number length, or the string '00' (zero zero) if there are no even length words



# Constraints

# 1 ≤ length of sentence ≤ 105
# The sentence string consists of spaces and letters in the range ascii[a-z, A-Z, ] only.


# Input Format for Custom Testing
# Input from stdin will be processed as follows and passed to the function.



# A single line of space-separated strings denoting sentence.



# Sample Case 0
# Sample Input 0

# STDIN                                Function
# --------------------------           -------------------------------
# It is a pleasant day today    →      sentence = "It is a pleasant day today"



# Sample Output 0

# pleasant


# Explanation 0

# There are three even length words: It (with length 2), is (2), and pleasant (8).



# Sample Case 1
# Sample Input 1

# STDIN                                    Function
# ------------------------------           -------------------------------
# You can do it the way you like    →     sentence = "You can do it the way you like"



# Sample Output 1

# like


# Explanation 1

# There are three even length words: do (with length 2), it (2), and like (4).


def longestEvenWord(sentence):
    words = sentence.split()
    longest_word = ""
    for word in words:
        if len(word) % 2 == 0 and len(word) > len(longest_word):
            longest_word = word
    if longest_word:
        return longest_word
    else:
        return "00"


sentence = "Time to write great code"
print(longestEvenWord(sentence))  # Output: Time

sentence = "It is a pleasant day today"
print(longestEvenWord(sentence))  # Output: pleasant

sentence = "You can do it the way you like bobo"
print(longestEvenWord(sentence))  # Output: like
