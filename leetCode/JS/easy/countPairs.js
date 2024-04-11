// https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/

// Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.


// ! Example 1:
// Input: nums = [3,1,2,2,2,1,3], k = 2
// Output: 4
// Explanation:
// There are 4 pairs that meet all the requirements:
// - nums[0] == nums[6], and 0 * 6 == 0, which is divisible by 2.
// - nums[2] == nums[3], and 2 * 3 == 6, which is divisible by 2.
// - nums[2] == nums[4], and 2 * 4 == 8, which is divisible by 2.
// - nums[3] == nums[4], and 3 * 4 == 12, which is divisible by 2.

// ! Example 2:
// Input: nums = [1,2,3,4], k = 1
// Output: 0
// Explanation: Since no value in nums is repeated, there are no pairs (i,j) that meet all the requirements.


// Constraints:

// 1 <= nums.length <= 100
// 1 <= nums[i], k <= 100

const countPairs = (nums, k) => {
    // Create a map to store indices of seen numbers
    const seen = new Map();
    // Get the length of the nums array
    const n = nums.length;
    // Initialize a count variable to store the number of pairs
    let count = 0;

    // Iterate through the nums array
    for (let i = 0; i < n; i++) {
        // Check if the current number has been seen before
        if (seen.has(nums[i])) {
            // If the number has been seen, iterate through the indices of its occurrences
            for (const value of seen.get(nums[i])) {
                // Check if the product of the current index and the previous index is divisible by k
                if ((i * value) % k === 0) {
                    // If divisible by k, increment the count of pairs
                    count++;
                }
            }
        }

        // If the current number is not in the map, add it with an empty array
        if (!seen.has(nums[i])) {
            seen.set(nums[i], []);
        }
        // Add the current index to the array of indices for the current number
        seen.get(nums[i]).push(i);
    }

    // Return the count of pairs that satisfy the condition
    return count;
}


// ! Example 1:
nums = [3, 1, 2, 2, 2, 1, 3]
k = 2
console.log(countPairs(nums, k))
// Output: 4
// Explanation:
// There are 4 pairs that meet all the requirements:
// - nums[0] == nums[6], and 0 * 6 == 0, which is divisible by 2.
// - nums[2] == nums[3], and 2 * 3 == 6, which is divisible by 2.
// - nums[2] == nums[4], and 2 * 4 == 8, which is divisible by 2.
// - nums[3] == nums[4], and 3 * 4 == 12, which is divisible by 2.

// ! Example 2:
nums = [1, 2, 3, 4]
k = 1
console.log(countPairs(nums, k))
// Output: 0
// Explanation: Since no value in nums is repeated, there are no pairs (i,j) that meet all the requirements.