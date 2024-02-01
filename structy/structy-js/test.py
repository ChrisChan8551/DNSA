#  1. Longest Even Length Word
#  Consider a string, sentence, of words separated by spaces where each word is a substring consisting of English alphabetic letters only. Find the first word in the sentence that has a length which is both an even number and greater than or equal to the length of any other word of even length in the sentence. If there are multiple words meeting the criteria, return the one which occurs first in the sentence.
#


#  Example

#  sentence = "Time to write great code"

#  The lengths of the words are 4, 2, 5, 5, 4, in order. The longest even length words are Time and code. The one that occurs first is Time, the answer to return



#  Function Description

#  Complete the function longestEvenWord in the editor below.



#  longestEvenWord has the following parameter(s):

#  string sentence:  a sentence string



#  Returns:

    #  string: the word that is first occurrence of a string with maximal even number length, or the string '00' (zero zero) if there are no even length words



#  Constraints

#  1 ≤ length of sentence ≤ 105
#  The sentence string consists of spaces and letters in the range ascii[a-z, A-Z, ] only.


#  Input Format for Custom Testing
#  Input from stdin will be processed as follows and passed to the function.



#  A single line of space-separated strings denoting sentence.



#  Sample Case 0
#  Sample Input 0

#  STDIN                                Function
#  --------------------------           -------------------------------
#  It is a pleasant day today    →      sentence = "It is a pleasant day today"



#  Sample Output 0

#  pleasant


#  Explanation 0

#  There are three even length words: It (with length 2), is (2), and pleasant (8).



#  Sample Case 1
#  Sample Input 1

#  STDIN                                    Function
#  ------------------------------           -------------------------------
#  You can do it the way you like    →     sentence = "You can do it the way you like"



#  Sample Output 1

#  like


#  Explanation 1

#  There are three even length words: do (with length 2), it (2), and like (4).
#

def longestEvenWord(sentence):
    words = sentence.split()
    longest_length = 0
    longest_word = ""

    for word in words:
        if len(word) % 2 == 0 and len(word) > longest_length:
            longest_length = len(word)
            longest_word = word

    if longest_length == 0:
        return '00'
    else:
        return longest_word


#  Two possible actions that give the minimum 2 different IDs:

#  Remove 2 items with ID = 2  and the final bag will contain item ids' = [1, 1, 1, 3]
#  Remove 1 item with ID = 2  and 1 item with ID=3 and the final bag will contain item ids' = [1, 1, 1, 2]


#  The minimum number of distinct IDs is 2.



#  Function Description

#  Complete the function deleteProducts in the editor below.



#  deleteProducts has the following parameters:

    #  int ids[n]:  an array of integers

    #  int m: an integer, the maximum number of deletions



#  Returns:

    #  int: an integer that represents the minimum number of item IDs



#  Constraints

#  1 ≤ n ≤ 105
#  1 ≤ ids[i] ≤ 106
#  1 ≤ m ≤ 105


#  Input Format For Custom Testing
#  The first line contains an integer, n, that denotes the number of elements in ids.
#  Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer ids[i].

#  The last line contains an integer, m, that denotes the maximum number of items that can be deleted.

#  Sample Case 0
#  Sample Input

#  STDIN    Function
#  -----    -----
#  4     →  ids[] size n = 4
#  1     →  ids = [1, 1, 5, 5]
#  1
#  5
#  5
#  2     →  m = 2
#  Sample Output

#  1
#  Explanation

#  Two possible actions that give 1 as the minimum number of different IDs:

#  Remove 2 items with ID = 1  and the final bag will contain item ids' = [5, 5]
#  Remove 2 items with ID = 5  and the final bag will contain item ids' = [1, 1]
#  Sample Case 1
#  Sample Input

#  STDIN    Function
#  -----    -----
#  7     →  ids[] size n = 7
#  1     →  ids = [1, 2, 3, 1, 2, 2, 1]
#  2
#  3
#  1
#  2
#  2
#  1
#  3    →   m = 3
#  Sample Output

#  2
#  Explanation

#  Three possible actions that give 2 as the minimum number of different IDs:

#  Remove 3 items with ID = 1  and the final bag will contain item ids' = [2, 3, 2, 2]
#  Remove 3 items with ID = 2  and the final bag will contain item ids' = [1, 3, 1, 1]
#  Remove 1 item with ID = 3  and the final bag will contain item ids' = [1, 2, 1, 2, 2, 1]

def deleteProducts(ids, m):
    frequency = {}
    for id in ids:
        frequency[id] = frequency.get(id, 0) + 1

    counts = sorted(frequency.values())

    while m > 0 and counts:
        remove = min(counts)
        if remove > m:
            break

        m -= remove
        counts.remove(remove)

    return len(counts)

# Testing with the provided input examples
ids = [1, 1, 5, 5]
m = 2
print(deleteProducts(ids, m))  # Output: 1

ids = [1, 2, 3, 1, 2, 2, 1]
m = 3
print(deleteProducts(ids, m))  # Output: 2

ids = [1, 2, 3, 1, 2, 2, 1, 3]
m = 1
print(deleteProducts(ids, m))  # Output: 2

ids = [1, 2, 3, 4]
m = 2
print(deleteProducts(ids, m))  # Output: 2

ids = [1, 2, 3, 4]
m = 1
print(deleteProducts(ids, m))  # Output: 3

##
