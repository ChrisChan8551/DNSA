function search(nums, target) {
	for (let i = 0; i < nums.length; i++) {
		if (nums[i] === target) {
			return i;
		}
	}
	return -1;
}

function search(nums, target) {
	let left = 0;
	let right = nums.length - 1;

	while (left <= right) {
		let mid = Math.floor((left + right) / 2);

		if (nums[mid] === target) {
			return mid;
		} else if (nums[mid] < target) {
			left = mid + 1;
		} else {
			right = mid - 1;
		}
	}

	return -1;
}

//o(log n) time complexity
