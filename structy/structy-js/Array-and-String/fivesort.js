// five sort
// Write a function, fiveSort, that takes in an array of numbers as an argument. The function should rearrange elements of the array such that all 5s appear at the end. Your function should perform this operation in-place by mutating the original array. The function should return the array.

// Elements that are not 5 can appear in any order in the output, as long as all 5s are at the end of the array.

// fiveSort([12, 5, 1, 5, 12, 7]);
// // -> [12, 7, 1, 12, 5, 5]
// fiveSort([5, 2, 5, 6, 5, 1, 10, 2, 5, 5]);
// // -> [2, 2, 10, 6, 1, 5, 5, 5, 5, 5]
// fiveSort([5, 5, 5, 1, 1, 1, 4]);
// // -> [4, 1, 1, 1, 5, 5, 5]
// fiveSort([5, 5, 6, 5, 5, 5, 5]);
// // -> [6, 5, 5, 5, 5, 5, 5]
// fiveSort([5, 1, 2, 5, 5, 3, 2, 5, 1, 5, 5, 5, 4, 5]);
// // -> [4, 1, 2, 1, 2, 3, 5, 5, 5, 5, 5, 5, 5, 5]
// const fives = new Array(20000).fill(5);
// const fours = new Array(20000).fill(4);
// const nums = [...fives, ...fours];

// fiveSort(nums);
// twenty-thousand 4s followed by twenty-thousand 5s
// -> [4, 4, 4, 4, ..., 5, 5, 5, 5]

//! O(n)
const fiveSort = (nums) => {
	let i = 0;
	let j = nums.length - 1;
	while (i < j) {
		if (nums[j] === 5) {
			j--;
		} else if (nums[i] === 5 && nums[j] !== 5) {
			let num1 = nums[i];
			let num2 = nums[j];
			nums[i] = num2;
			nums[j] = num1;
			// [nums[i], nums[j]] = [nums[j], nums[i]];
			i++;
		} else {
			i++;
		}
	}
	return nums;
};


// fiveSort([12, 5, 1, 5, 12, 7]);
// // -> [12, 7, 1, 12, 5, 5]
// fiveSort([5, 2, 5, 6, 5, 1, 10, 2, 5, 5]);
// // -> [2, 2, 10, 6, 1, 5, 5, 5, 5, 5]
// fiveSort([5, 5, 5, 1, 1, 1, 4]);
// // -> [4, 1, 1, 1, 5, 5, 5]
// fiveSort([5, 5, 6, 5, 5, 5, 5]);
// // -> [6, 5, 5, 5, 5, 5, 5]
// fiveSort([5, 1, 2, 5, 5, 3, 2, 5, 1, 5, 5, 5, 4, 5]);
// // -> [4, 1, 2, 1, 2, 3, 5, 5, 5, 5, 5, 5, 5, 5]
// const fives = new Array(20000).fill(5);
// const fours = new Array(20000).fill(4);
// const nums = [...fives, ...fours];

// fiveSort(nums);
// twenty-thousand 4s followed by twenty-thousand 5s
// -> [4, 4, 4, 4, ..., 5, 5, 5, 5]

// console.log(fiveSort([12, 5, 1, 5, 12, 7])); // -> [12, 7, 1, 12, 5, 5]
// console.log(fiveSort([5, 2, 5, 6, 5, 1, 10, 2, 5, 5])); // -> [2, 2, 10, 6, 1, 5, 5, 5, 5, 5]
// console.log(fiveSort([5, 5, 5, 1, 1, 1, 4])); // -> [4, 1, 1, 1, 5, 5, 5]
// console.log(fiveSort([5, 5, 6, 5, 5, 5, 5])); // -> [6, 5, 5, 5, 5, 5, 5]
// console.log(fiveSort([5, 1, 2, 5, 5, 3, 2, 5, 1, 5, 5, 5, 4, 5])); // -> [4, 1, 2, 1, 2, 3, 5, 5, 5, 5, 5, 5, 5, 5]
//
