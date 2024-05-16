# https://leetcode.com/problems/non-overlapping-intervals/


# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.


#! Example 1:
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

#! Example 2:
# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

#! Example 3:
# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


# Constraints:

# 1 <= intervals.length <= 105
# intervals[i].length == 2
# -5 * 104 <= starti < endi <= 5 * 104


def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: x[1])
    end = intervals[0][1]
    removed = 0
    for i in range(1, len(intervals)):
        if intervals[i][0] < end:
            removed += 1
        else:
            end = intervals[i][1]
    return removed


#! Example 1:
intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(eraseOverlapIntervals(intervals))
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

#! Example 2:
intervals = [[1, 2], [1, 2], [1, 2]]
print(eraseOverlapIntervals(intervals))
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

#! Example 3:
intervals = [[1, 2], [2, 3]]
print(eraseOverlapIntervals(intervals))
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
