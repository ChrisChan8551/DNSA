// Write a function, bottomRightValue, that takes in the root of a binary tree. The function should return the right-most value in the bottom-most level of the tree.

// You may assume that the input tree is non-empty.

class Node {
	constructor(val) {
		this.val = val;
		this.left = null;
		this.right = null;
	}
}

// const bottomRightValue = (root) => {
// 	// if (root.left === null && root.right === null) return root.val;
// 	// const queue = [root];
// 	// let current = null; // have to declare the current on outside so you have access to it outside of the loop
// 	// while (queue.length > 0) {
// 	// 	current = queue.shift();
// 	// 	if (current.left !== null) queue.push(current.left);
// 	// 	if (current.right !== null) queue.push(current.right);
// 	// }
// 	// return current.val;
// };

//! alternative if you want to follow the traditional while loop
const bottomRightValue = (root) => {
	if (root.left === null && root.right === null) return root.val;
	const queue = [root];
	while (queue.length > 0) {
		const current = queue.shift();
		if (current.left !== null) queue.push(current.left);
		if (current.right !== null) queue.push(current.right);
		if ((queue.length = 0)) return current.val;
	}
};

//! TEST_00
const a = new Node(3);
const b = new Node(11);
const c = new Node(10);
const d = new Node(4);
const e = new Node(-2);
const f = new Node(1);

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;

//       3
//    /    \
//   11     10
//  / \      \
// 4   -2     1

console.log(bottomRightValue(a)); // -> 1

//! TEST_01
// const a = new Node(-1);
// const b = new Node(-6);
// const c = new Node(-5);
// const d = new Node(-3);
// const e = new Node(-4);
// const f = new Node(-13);
// const g = new Node(-2);
// const h = new Node(6);

// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// e.right = h;

// //        -1
// //      /   \
// //    -6    -5
// //   /  \     \
// // -3   -4   -13
// //     / \
// //    -2  6

// bottomRightValue(a); // -> 6

//! TEST_02
// const a = new Node(-1);
// const b = new Node(-6);
// const c = new Node(-5);
// const d = new Node(-3);
// const e = new Node(-4);
// const f = new Node(-13);
// const g = new Node(-2);
// const h = new Node(6);
// const i = new Node(7);

// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// e.right = h;
// f.left = i;

// //        -1
// //      /   \
// //    -6    -5
// //   /  \     \
// // -3   -4   -13
// //     / \    /
// //    -2  6  7

// bottomRightValue(a); // -> 7

//! TEST_03
// const a = new Node('a');
// const b = new Node('b');
// const c = new Node('c');
// const d = new Node('d');
// const e = new Node('e');
// const f = new Node('f');

// a.left = b;
// a.right = c;
// b.right = d;
// d.left = e;
// e.right = f;

// //      a
// //    /   \
// //   b     c
// //    \
// //     d
// //    /
// //   e
// //   \
// //    f

// bottomRightValue(a); // -> 'f'

//! TEST_04
// const a = new Node(42);

// //      42

// console.log(bottomRightValue(a)); // -> 42
