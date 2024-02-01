#  2. Selling Products
#  A salesperson must sell n items in a bag with random IDs. The salesperson can remove as many as m items from the bag. Determine the minimum number of different IDs the final bag can contain after performing, at most, m deletions.


#  Example

#  n = 6

#  ids = [1, 1, 1, 2, 3, 2]

#  m = 2


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

from collections import Counter

def deleteProducts(ids, m):
    frequency = {}
    min_count = 0

    # Count the frequency of each ID
    for id in ids:
        if id in frequency:
            frequency[id] += 1
        else:
            frequency[id] = 1

    # Find the minimum frequency count
    for count in frequency.values():
        if count < min_count:
            min_count = count

    # Calculate the remaining distinct IDs
    count = 0
    for freq in frequency.values():
        if freq > min_count:
            count += 1

    return count




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
