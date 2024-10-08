# An array of size n represents a set of available resources. Identify a
# subarray that optimally utilizes these resources under the following
# constraints:
# • The subarray must have a specific length, denoted ask.
# • All elements in the subarray must be unique, representing distinct
# resource allocations.
# The ultimate goal is to f ind the su bar ray that maximizes the sum o·
# the allocated resources. Return t he sum for that subarray. If it is nc
# possible to allocate resources per the constraints, return -1.
# Note: A subarray is a contiguous segment of an array.
# Example
# n = 5
# k = 3
# arr = [1, 2, 3, 7, 3, 5)
# Following are the subarrays of length k = 3 and all elements are
# distinct:
# • (1, 2, 3], and 1 + 2 + 3 = 6
# • (2, 3, 7], sum = 12
# • (7, 3, 5],sum = 1 s
# Return the maximum sum, 15.
# Function Description
# Complete the function findOptima/Resources in the editor below.
# findOptima/Resources has the following parameter(s):
# int arr[n]: the set of available resources
# int k:the size of the subarray
# Returns
# long. maximum sum of any subarray that meets the criteria, or -1
# if no such subarray is possible
# Constraints
# 1 <= k <= n <= 2 * 10 ^ 5
# 1 <= arr[i] <= 10 ^ 9


def max_unique_subarray_sum(arr, k):
    n = len(arr)
    if k > n:
        return -1

    max_sum = -1
    current_sum = 0
    left = 0
    unique = {}

    for right in range(n):

        while arr[right] in unique and unique[arr[right]] > 0:
            unique[arr[left]] -= 1
            current_sum -= arr[left]
            if unique[arr[left]] == 0:
                del unique[arr[left]]
            left += 1

        if arr[right] not in unique:
            unique[arr[right]] = 0
        unique[arr[right]] += 1
        current_sum += arr[right]

        if right - left + 1 == k:
            max_sum = max(max_sum, current_sum)

            unique[arr[left]] -= 1
            current_sum -= arr[left]
            if unique[arr[left]] == 0:
                del unique[arr[left]]
            left += 1

    return max_sum if max_sum != -1 else -1


# Example usage
n = 5
k = 3
arr = [1, 2, 3, 7, 3, 5]
result = max_unique_subarray_sum(arr, k)
print(result)  # Output: 15


# A string is a pangram if it contains all letters of the English alphabet,
# ascii['a'-'z']. Given a list of strings, determine if each one is a
# pangram or not. Return "1" if true and "0" if false.
# Example
# pangram = ['pack my box with five dozen liquor jugs; 'this is not a
# pangram')
# • The string 'pack my box with five dozen liquor jugs' is a
# pangram because it contains all the letters 'a' through 'z'.
# • The string 'this is not a pangram' is not a pangram.
# • Assemble a string of the two results, in order. The result is '10'.
# Function Description Complete the function isPangram in the
# editor below.
# isPangram has the following parameter(s):
# string pangram[n]: the sentences to check
# Returns
# string: a string where each posit ion represents the results of a
# test. Use ' 1' for true and '0' for false.
# Constraints
# • 1 <= n <= 100
# • Each string pangram[i](where 0 <= i < n) is composed of lowercase
# letters and spaces.
# • 1 <= length of pangram[i] <= 10 ^ 5


def isPangram(pangram):
    result = []
    alpha = set('abcdefghijklmnopqrstuvwxyz')

    for words in pangram:

        uniqueChar = set()
        for char in words:
            if char.isalpha():
                uniqueChar.add(char)

        if alpha <= uniqueChar:
            result.append('1')
        else:
            result.append('0')

    return ''.join(result)


# Example usage
pangram_list = ['pack my box with five dozen liquor jugs',
                'this is not a pangram']
result = isPangram(pangram_list)
print(result)  # Output: '10'
