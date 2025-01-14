// Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

// Notice that the solution set must not contain duplicate triplets.

//! Example 1:
// Input: nums = [-1,0,1,2,-1,-4]
// Output: [[-1,-1,2],[-1,0,1]]
// Explanation:
// nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
// nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
// nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
// The distinct triplets are [-1,0,1] and [-1,-1,2].
// Notice that the order of the output and the order of the triplets does not matter.

//! Example 2:
// Input: nums = [0,1,1]
// Output: []
// Explanation: The only possible triplet does not sum up to 0.

//! Example 3:
// Input: nums = [0,0,0]
// Output: [[0,0,0]]
// Explanation: The only possible triplet sums up to 0.

// Constraints:

// 3 <= nums.length <= 3000
// -105 <= nums[i] <= 105

//! brute force
// var threeSum = function (nums) {
// 	const res = [];
// 	const seen = new Set(); // To track unique triplets

// 	nums.sort((a, b) => a - b); // Sort the array

// 	for (let i = 0; i < nums.length; i++) {
// 		for (let j = i + 1; j < nums.length; j++) {
// 			for (let k = j + 1; k < nums.length; k++) {
// 				if (nums[i] + nums[j] + nums[k] === 0) {
// 					const triplet = [nums[i], nums[j], nums[k]];
// 					const key = triplet.join(','); // Serialize as a string
// 					if (!seen.has(key)) {
// 						seen.add(key); // Add the string to the Set
// 						res.push(triplet); // Push the actual array to the result
// 					}
// 				}
// 			}
// 		}
// 	}

// 	return res;
// };

//! 2 pointer

var threeSum = function (nums) {
	// Step 1: Sort the array
	nums.sort((a, b) => a - b);
	let res = [];

	for (let i = 0; i < nums.length; i++) {
		// Step 2: Skip duplicates for the first number
		if (i > 0 && nums[i] === nums[i - 1]) continue;
		let left = i + 1;
		let right = nums.length - 1;
		while (left < right) {
			const sum = nums[i] + nums[left] + nums[right];
			if (sum === 0) {
				res.push([nums[i], nums[left], nums[right]]);
				// Move pointers to skip duplicates
				while (left < right && nums[left] === nums[left + 1]) left++;
				while (left < right && nums[right] === nums[right - 1]) right--;
				left++;
				right--;
			} else if (sum < 0) {
				left++; // Sum is too small; move left pointer to increase it
			} else {
				right--; // Sum is too large; move right pointer to decrease it
			}
		}
	}
	return res;
};

//! Example 1:
nums = [-1, 0, 1, 2, -1, -4];
console.log(threeSum(nums));
// Output: [[-1,-1,2],[-1,0,1]]
// Explanation:
// nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
// nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
// nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
// The distinct triplets are [-1,0,1] and [-1,-1,2].
// Notice that the order of the output and the order of the triplets does not matter.

//! Example 2:
nums = [0, 1, 1];
console.log(threeSum(nums));
// Output: []
// Explanation: The only possible triplet does not sum up to 0.

//! Example 3:
nums = [0, 0, 0];
console.log(threeSum(nums));
// Output: [[0,0,0]]
// Explanation: The only possible triplet sums up to 0.
