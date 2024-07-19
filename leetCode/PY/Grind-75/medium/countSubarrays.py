# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/


# You are given an integer array nums and a positive integer k.

# Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

# A subarray is a contiguous sequence of elements within an array.


#! Example 1:
# Input: nums = [1,3,2,3,3], k = 2
# Output: 6
# Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].

#! Example 2:
# Input: nums = [1,4,2,1], k = 3
# Output: 0
# Explanation: No subarray contains the element 4 at least 3 times.


# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 106
# 1 <= k <= 105

# def countSubarrays(nums, k):
#     max_num = max(nums)
#     count = 0
#     left = 0
#     cnt_subarr = 0

#     # move right pointer each time
#     for right in range(len(nums)):
#         if nums[right] == max_num:
#             count += 1

#         # left pointer moves until condition is satisfied
#         while count >= k:
#             cnt_subarr += len(nums) - right

#             if nums[left] == max_num:
#                 count -= 1
#             left += 1

#     return cnt_subarr

#! souldude solution
# def countSubarrays(nums, k):
#     max_num = max(nums)
#     count = 0
#     left = nums.index(max_num)
#     cnt_subarr = 0

#     # move right pointer each time
#     for right in range(left, len(nums)):
#         if nums[right] == max_num:
#             count += 1

#         # left pointer moves until condition is satisfied
#         while count > k:
#             left += 1

#             if nums[left] == max_num:
#                 count -= 1

#         if count == k:
#             cnt_subarr += left + 1

#     return cnt_subarr

#! chatGPT solution
def countSubarrays(nums, k):
    # 1. Get the length of the array to know the range for indices and to help count valid subarrays.
    n = len(nums)
    # 2. Find the maximum number in the array, as we need to count subarrays where this number appears at least k times.
    max_num = max(nums)
    left = 0  # 3. Initialize the left pointer of the sliding window.
    # 4. Initialize a counter to keep track of the occurrences of max_num within the current window.
    count = 0
    # 5. Initialize result to store the total count of valid subarrays.
    result = 0

    # Iterate through the array with the right pointer
    # 6. Start iterating with the right pointer from the beginning to the end of the array.
    for right in range(n):
        # 7. Check if the current element at the right pointer is the maximum number.
        if nums[right] == max_num:
            # 8. If it is, increment the count of max_num occurrences within the window.
            count += 1

        # Adjust the left pointer to ensure the window has at least k occurrences of max_num
        while count >= k:  # 9. As long as the count of max_num is at least k, the window is valid.
            # 10. Count all valid subarrays ending at the current right pointer. Since subarrays can start from any index between left and right.
            result += n - right
            # 11. Before moving the left pointer, check if the element at the left pointer is max_num.
            if nums[left] == max_num:
                # 12. If it is, decrement the count of max_num as this element will no longer be in the window.
                count -= 1
            # 13. Move the left pointer to the right to potentially find a new valid window.
            left += 1

    return result  # 14. Return the total count of valid subarrays.


#! Example 1:
nums = [1, 3, 2, 3, 3]
k = 2
print(countSubarrays(nums, k))
# Output: 6
# Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].

#! Example 2:
nums = [1, 4, 2, 1]
k = 3
print(countSubarrays(nums, k))
# Output: 0
# Explanation: No subarray contains the element 4 at least 3 times.
