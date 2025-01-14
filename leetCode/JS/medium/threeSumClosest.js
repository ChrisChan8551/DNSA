// https://leetcode.com/problems/3sum-closest/

// Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

// Return the sum of the three integers.

// You may assume that each input would have exactly one solution.

//! Example 1:
// Input: nums = [-1,2,1,-4], target = 1
// Output: 2
// Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

//! Example 2:
// Input: nums = [0,0,0], target = 1
// Output: 0
// Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

// Constraints:

// 3 <= nums.length <= 500
// -1000 <= nums[i] <= 1000
// -104 <= target <= 104

//! 2 pointer
const threeSumClosest = (nums, target) => {
	// similar to 3sum problem.
	// declare result and set it to Infinity since we're looking for closest sum.
	// loop through the nums array
	// set left and right pointers
	// will need to sort the nums array
	// to check what is the closest by absolute value subtracting (target and the sum) vs (current result vs sum)
	let result = Infinity;
	nums.sort((a, b) => a - b);
	for (let i = 0; i < nums.length - 2; i++) {
		let [left, right] = [i + 1, nums.length - 1];
		while (left < right) {
			let sum = nums[i] + nums[left] + nums[right];
			//update the result if it finds a lower difference.
			if (Math.abs(target - sum) < Math.abs(result - target)) {
				result = sum;
			}
			if (sum < target) {
				left++;
			} else if (sum > target) {
				right--;
				// If the current sum equals the target, return it immediately
			} else {
				return sum;
			}
		}
	}
	return result;
};

//! Example 1:
(nums = [-1, 2, 1, -4]), (target = 1);
console.log(threeSumClosest(nums, target));
// Output: 2
// Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

//! Example 2:
(nums = [0, 0, 0]), (target = 1);
console.log(threeSumClosest(nums, target));
// Output: 0
// Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
