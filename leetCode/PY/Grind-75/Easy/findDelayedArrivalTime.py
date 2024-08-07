# https://leetcode.com/problems/calculate-delayed-arrival-time/

# You are given a positive integer arrivalTime denoting the arrival time of a train in hours, and another positive integer delayedTime denoting the amount of delay in hours.

# Return the time when the train will arrive at the station.

# Note that the time in this problem is in 24-hours format.


#! Example 1:
# Input: arrivalTime = 15, delayedTime = 5
# Output: 20
# Explanation: Arrival time of the train was 15:00 hours. It is delayed by 5 hours. Now it will reach at 15+5 = 20 (20:00 hours).

#! Example 2:
# Input: arrivalTime = 13, delayedTime = 11
# Output: 0
# Explanation: Arrival time of the train was 13:00 hours. It is delayed by 11 hours. Now it will reach at 13+11=24 (Which is denoted by 00:00 in 24 hours format so return 0).


# Constraints:

# 1 <= arrivaltime < 24
# 1 <= delayedTime <= 24
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 52.4K
# Submissions
# 66.8K
# Acceptance Rate
# 78.5%
# Topics
# Companies
# Hint 1
# Use the modulo operator to handle the case when the arrival time plus the delayed time goes beyond 24 hours.
# Hint 2
# If the arrival time plus the delayed time is greater than or equal to 24, you can also subtract 24 to get the time in the 24-hour format.
# Hint 3
# Use the modulo operator to handle the case when the arrival time plus the delayed time goes beyond 24 hours.
# Hint 4
# If the arrival time plus the delayed time is greater than or equal to 24, you can also subtract 24 to get the time in the 24-hour format.


# def findDelayedArrivalTime(arrivalTime, delayedTime):
#     totalTime = arrivalTime + delayedTime
#     if totalTime == 24:
#         return 0
#     elif totalTime < 24:
#         return totalTime
#     elif totalTime > 24:
#         day = totalTime % 24
#         return day

def findDelayedArrivalTime(arrivalTime, delayedTime):
    return (arrivalTime + delayedTime) % 24

#! Example 1:
arrivalTime = 15
delayedTime = 5
print(findDelayedArrivalTime(arrivalTime, delayedTime))
# Output: 20
# Explanation: Arrival time of the train was 15:00 hours. It is delayed by 5 hours. Now it will reach at 15+5 = 20 (20:00 hours).

#! Example 2:
arrivalTime = 13
delayedTime = 11
print(findDelayedArrivalTime(arrivalTime, delayedTime))
# Output: 0
# Explanation: Arrival time of the train was 13:00 hours. It is delayed by 11 hours. Now it will reach at 13+11=24 (Which is denoted by 00:00 in 24 hours format so return 0).
