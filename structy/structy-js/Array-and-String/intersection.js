// intersection
// Write a function, intersection, that takes in two arrays, a,b, as arguments. The function should return a new array containing elements that are in both of the two arrays.

// You may assume that each input array does not contain duplicate elements.

// //!O(n^2) time complexity
// const intersection = (a, b) => {
// 	let intersect = [];

// 	for (let i = 0; i < a.length; i++) {
// 		for (let j = 0; j < b.length; j++) {
// 			if (a[i] === b[j]) {
// 				intersect.push(a[i]);
// 			}
// 		}
// 	}
// 	return intersect;
// };
//!O(n^2) time complexity
// const intersection = (a, b) => {
// 	let intersect = [];

// 	for (let item of a) {
// 		if (b.includes(item)) {
// 			intersect.push(item);
// 		}
// 	}
// 	return intersect;
// };

//O(n) time complexity
// const intersection = (a, b) => {
// 	let intersect = [];
// 	let setA = new Set(a);
// 	for (let i of b) {
// 		if (setA.has(i)) {
//! has is O(1) runtime complexity
// 			intersect.push(i);
// 		}
// 	}
// 	return intersect;
// };

//! TEST_00
// intersection([4,2,1,6], [3,6,9,2,10]) // -> [2,6]

//! TEST_01
// intersection([2,4,6], [4,2]) // -> [2,4]

//! TEST_02
// intersection([4,2,1], [1,2,4,6]) // -> [1,2,4]

//! TEST_03
// intersection([0,1,2], [10,11]) // -> []

//! TEST_04
// const a = [];
// const b = [];
// for (let i = 0; i < 50000; i += 1) {
//   a.push(i);
//   b.push(i);
// }
// intersection(a, b) // -> [0,1,2,3,..., 49999]
