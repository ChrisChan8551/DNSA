// pair product
// Write a function, pairProduct, that takes in an array and a target product as arguments. The function should return an array containing a pair of indices whose elements multiply to the given target. The indices returned must be unique.

// Be sure to return the indices, not the elements themselves.

// There is guaranteed to be one such pair whose product is the target.

// pairProduct([3, 2, 5, 4, 1], 8); // -> [1, 3]
// pairProduct([3, 2, 5, 4, 1], 10); // -> [1, 2]
// pairProduct([4, 7, 9, 2, 5, 1], 5); // -> [4, 5]
// pairProduct([4, 7, 9, 2, 5, 1], 35); // -> [1, 4]
// pairProduct([3, 2, 5, 4, 1], 10); // -> [1, 2]
// pairProduct([4, 6, 8, 2], 16); // -> [2, 3]

//! o(n^2)
// const pairProduct = (numbers, targetProduct) => {
// 	let array = [];
// 	for (let i = 0; i < numbers.length; i++) {
// 		for (let j = i + 1; j < numbers.length; j++) {
// 			if (numbers[i] * numbers[j] === targetProduct) {
// 				return [i, j];
// 			}
// 		}
// 	}
// };

const pairProduct = (numbers, targetProduct) => {
	const prev = {};
	for (let i = 0; i < numbers.length; i++) {
		const num = numbers[i];
		const complement = targetProduct / num;
		if (complement in prev) {
			return [prev[complement],i];
		}
		prev[num] = i;
	}
};

console.log(pairProduct([3, 2, 5, 4, 1], 10)); // -> [1, 2]
console.log(pairProduct([4, 7, 9, 2, 5, 1], 5)); // -> [4, 5]
console.log(pairProduct([4, 7, 9, 2, 5, 1], 35)); // -> [1, 4]
console.log(pairProduct([3, 2, 5, 4, 1], 10)); // -> [1, 2]
console.log(pairProduct([4, 6, 8, 2], 16)); // -> [2, 3]
