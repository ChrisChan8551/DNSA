# HackerRank

# A start-up owner is looking to meet new investors to get some funds
# for his company. Each investor has a tight schedule that the owner
# has to respect. Given the schedules of the days investors are
# available, determine how many meetings the owner can schedule.
# Note that the owner can only have one meeting per day.
# The schedules consists of two integer arrays, firstDay and /astDay.
# Each element in the array firstDay represents the first day an
# investor is available, and each element in /astDay represents the last
# day an investor is available, both inclusive.
# Example:
# firstDay = (1,2,3,3,3]
# /astDay= (2,2,3,4,4]
# • There are 5 investors [1-0. 1- 1. 1-2, 1-3. 1-4]
# • The investor 1-0 is available from day 1 to day 2 inclusive [1 , 2]
# • The investor 1-1 is available in day 2 only [2. 2]. The investor 1-2 is
# available in day 3 only (3, 3]
# • The investors 1-3 and 1-4 are available from d ay 3 to day 4 only [3. 4]
# • The owner can only meet 4 investors out of 5 : 1-0 in day 1. 1-1 in d ay 2,
# 1-2 in day 3 and 1-3 in day 4. The graphic below shows the scheduled
# meetings in green and blocked days are in gray.


# Function Description
# Complete the function countMeetings in the editor below.
# countMeetings has the following parameters:
# int firstDay[n]: an array of integers where the value of each
# element firstDay[i] is the first day the ith investor is available to
# meet.
# int lastDay[n] an array of integers where the value of each
# element lastDay[i] is the last day the ith investor is available to meet.
# Returns:
# int: an integer that represents the maximum number of meetings
# possible.
# Constraints
# • 1 <= n <= 10^5
# • 1 <= firstDay[i], lastDay[i] <= 10^5 (where O <= i < n)
# • firstDay[i] <= lastDay[i] (where O <= i < n)

# Example 1
# firstDay = [1,1,2]
# lastDay = [1,2,2]
# output = 2
# day 1 = {1,1}
# day 2 = {1,2}
# day 3 = {2,2}


def countMeetings(firstDay, lastDay):
    # create a list of tuples looping through firstDay, lastDay
    schedule = list(zip(firstDay, lastDay))
    # sort the list by the lastDay, or index 1 of the tuple

    #! instead of zip, you can use an array.
    # schedule = []
    # for i in range(len(firstDay)):
    #     schedule.append(firstDay[i], lastDay[i])

    schedule.sort(key=lambda x: x[1])
    # initialize count variable
    count = 0
    # initialize a set to keep track of availability throughout the days.
    # if it's available then add to set.
    # else break
    available = set()
    #loop through the start,end
    for start, end in schedule:
        #then you loop through the start and end days to determine if the 'day' is in the available set
        for day in range(start, end + 1):
            if day not in available:
                available.add(day)
                count += 1
                break
    return count


#! Example 1
firstDay = [1, 1, 2]
lastDay = [1, 2, 2]
print(countMeetings(firstDay, lastDay))
# output = 2

#! Example 2
firstDay = [1, 2, 1, 2, 2]
lastDay = [3, 2, 1, 3, 3]
print(countMeetings(firstDay, lastDay))
# output = 3
