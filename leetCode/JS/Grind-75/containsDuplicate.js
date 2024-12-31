// https://leetcode.com/problems/contains-duplicate/

// Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

// Constraints:
// 1 <= nums.length <= 105
// -109 <= nums[i] <= 109

// var containsDuplicate = function (nums) {
// 	let unique = {};
// 	for (let i = 0; i < nums.length; i++) {
// 		if (!unique[nums[i]]) {
// 			unique[nums[i]] = 1;
// 		} else {
// 			unique[nums[i]]++;
// 		}
// 		if (unique[nums[i]] > 1) return true;
// 	}
// 	return false;
// };

var containsDuplicate = function (nums) {
	let unique = new Set();
	for (let i = 0; i < nums.length; i++) {
		if (unique.has(nums[i])) {
			return true;
		} else {
			unique.add(nums[i]);
		}
	}
	return false;
};

//! Example 1:
nums = [1, 2, 3, 1];
console.log(containsDuplicate(nums));
// Output: true
// Explanation:
// The element 1 occurs at the indices 0 and 3.

//! Example 2:
nums = [1, 2, 3, 4];
console.log(containsDuplicate(nums));
// Output: false
// Explanation:
// All elements are distinct.

//! Example 3:
nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2];
console.log(containsDuplicate(nums));
// Output: true
