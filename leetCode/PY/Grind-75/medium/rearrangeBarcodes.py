
# https://leetcode.com/problems/distant-barcodes/

# In a warehouse, there is a row of barcodes, where the ith barcode is barcodes[i].

# Rearrange the barcodes so that no two adjacent barcodes are equal. You may return any answer, and it is guaranteed an answer exists.


#! Example 1:
# Input: barcodes = [1,1,1,2,2,2]
# Output: [2,1,2,1,2,1]

#! Example 2:
# Input: barcodes = [1,1,1,1,2,2,3,3]
# Output: [1,3,1,3,1,2,1,2]


# Constraints:

# 1 <= barcodes.length <= 10000
# 1 <= barcodes[i] <= 10000

import heapq
from collections import Counter

def rearrangeBarcodes(barcodes):
    # dictionary to keep track of frequencies
    # use a tuple for (freq, val) into a heap
    # prioritize taking highest frequency value.
    # if next value freq, matches previous value, move to next highest freq.
    frequency = Counter(barcodes)
    max_heap = []
    res = []

    for key in frequency:
        freq = -frequency[key]
        heapq.heappush(max_heap, (freq, key))

    while max_heap:
        freq1, num1 = heapq.heappop(max_heap)

        if len(res) == 0 or res[-1] != num1:
            res.append(num1)
            freq1 += 1

        else:
            freq2, num2 = heapq.heappop(max_heap)
            res.append(num2)
            freq2 += 1

            if freq2 != 0:
                heapq.heappush(max_heap, (freq2, num2))

        if freq1 != 0:
                heapq.heappush(max_heap, (freq1, num1))


    return res


#! Example 1:
barcodes = [1, 1, 1, 2, 2, 2]
print(rearrangeBarcodes(barcodes))
# Output: [2,1,2,1,2,1]

#! Example 2:
barcodes = [1, 1, 1, 1, 2, 2, 3, 3]
print(rearrangeBarcodes(barcodes))
# Output: [1,3,1,3,1,2,1,2]
