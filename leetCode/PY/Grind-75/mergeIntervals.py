# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.


# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.


# Constraints:

# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

def merge(intervals):
    intervals.sort()
    stack = [intervals[0]]  # start stack with first interval
    for i in range(1, len(intervals)):  # loop through the intervals
        current_interval = {
            'start': intervals[i][0],
            'end': intervals[i][1]
        }
        last_interval_index = len(stack)-1
        last_int = {
            # 'start': stack[last_interval_index][0],
            # 'end': stack[last_interval_index][1]
            'start': stack[-1][0],
            'end': stack[-1][1]
        }
        if current_interval['start'] <= last_int['end'] and current_interval['end'] > last_int['end']:
            # partially overlapping
            stack[last_interval_index][1] = current_interval['end']
        elif current_interval['start'] > last_int['end']:  # not overlapping
            stack.append(intervals[i])
    return stack

# make sure that the intervals are sorted
# partially overlap - change the first end point with the 2nd end point [1, 3], [2, 6] -> [1,6]
# no overlap - push the intervals into the result array
# complete overlap - because we sorted by start, only concerned with previous start interval


print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
# Output: [[1,6],[8,10],[15,18]]

print(merge([[1, 4], [4, 5]]))  # Output: [[1,5]]

print(merge([[1, 3], [2, 6], [8, 10], [15, 18], [1, 29]]))  # Output: [[1,29]]
