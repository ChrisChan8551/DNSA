# https://leetcode.com/problems/task-scheduler/

# You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.

# ​Return the minimum number of intervals required to complete all tasks.

#! Example 1:
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
# After completing task A, you must wait two cycles before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th cycle, you can do A again as 2 intervals have passed.

#! Example 2:
# Input: tasks = ["A","C","A","B","D","B"], n = 1
# Output: 6
# Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
# With a cooling interval of 1, you can repeat a task after just one other task.

#! Example 3:
# Input: tasks = ["A","A","A", "B","B","B"], n = 3
# Output: 10
# Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.
# There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.


# Constraints:
# 1 <= tasks.length <= 104
# tasks[i] is an uppercase English letter.
# 0 <= n <= 100

#! Hint 1
# There are many different solutions for this problem, including a greedy algorithm.

#! Hint 2
# For every cycle, find the most frequent letter that can be placed in this cycle. After placing, decrease the frequency of that letter by one.

from collections import defaultdict, deque
import heapq
from typing import Counter


def leastInterval(tasks, n):
    # keep track of freq (wait time, #tasks)
    # each time we add task to sequence, set wait time to n, and reduce all others by -1
    # iterate through dict, add to sequence, reduce freq of each task
    # if total tasks < n, then add (n - total tasks) to sequence
    # prioritize doing tasks with higher frequency
    # a heap / priority queue would allow us to keep track of highest freq at all times
    # pop off from heap, and increase val by 1
    # we can calculate the time for when we can next do a task (expiration time)
    # keep track of time passed since the first task
    task_freq = defaultdict(int)
    queue = deque()
    for task in tasks:
        task_freq[task] -= 1
    time = 0

    heap = list(task_freq.values())
    heapq.heapify(heap)
    queue = deque()

    while heap or queue:

        if heap:
            freq = heapq.heappop(heap) + 1
            if freq != 0:
                queue.append((freq, time + n))

        if queue and queue[0][1] == time:
            completed_freq, expiration_time = queue.popleft()
            heapq.heappush(heap, completed_freq)

        time += 1

    return time


#! Example 1:
tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
print(leastInterval(tasks, n))
# Output: 8
# Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
# After completing task A, you must wait two cycles before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th cycle, you can do A again as 2 intervals have passed.

#! Example 2:
tasks = ["A", "C", "A", "B", "D", "B"]
n = 1
print(leastInterval(tasks, n))
# Output: 6
# Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
# With a cooling interval of 1, you can repeat a task after just one other task.

#! Example 3:
tasks = ["A", "A", "A", "B", "B", "B"]
n = 3
print(leastInterval(tasks, n))
# Output: 10
# Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.
# There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.
