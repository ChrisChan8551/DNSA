// Write a function, howHigh, that takes in the node of a binary tree. The function should return a number representing the height of the tree.

// The height of a binary tree is defined as the maximal number of edges from the root node to any leaf node.

// If the tree is empty, return -1.

class Node {
	constructor(val) {
		this.val = val;
		this.left = null;
		this.right = null;
	}
}

//! recursive
// const howHigh = (node) => {
// 	// todo
// 	// if tree is empty, return -1;
// 	if (node === null) return -1;
// 	// if tree only has 1 node, return 0;
// 	// transverse through the tree and count edges

// 	const leftValues = howHigh(node.left);
// 	const rightValues = howHigh(node.right);
// 	return Math.max(leftValues, rightValues) + 1;
// };

//! interative

const howHigh = (node) => {
	if (node === null) return -1;
	let height = -1;
	const queue = [node];
	while (queue.length > 0) {
		const levelSize = queue.length;
		for (let i = 0; i < levelSize; i++) {
			const current = queue.shift();
			if (current.left !== null) {
				queue.push(current.left);
			}
			if (current.right !== null) {
				queue.push(current.right);
			}
		}
		height++;
	}
};

//! TEST_00
const a = new Node('a');
const b = new Node('b');
const c = new Node('c');
const d = new Node('d');
const e = new Node('e');
const f = new Node('f');

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;

//      a
//    /   \
//   b     c
//  / \     \
// d   e     f

console.log(howHigh(a)); // -> 2

//! TEST_01
// const a = new Node('a');
// const b = new Node('b');
// const c = new Node('c');
// const d = new Node('d');
// const e = new Node('e');
// const f = new Node('f');
// const g = new Node('g');

// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g

// //      a
// //    /   \
// //   b     c
// //  / \     \
// // d   e     f
// //    /
// //   g

// howHigh(a); // -> 3

//! TEST_02
// const a = new Node('a');
// const c = new Node('c');

// a.right = c;

// //      a
// //       \
// //        c

// howHigh(a); // -> 1

//! TEST_03
// const a = new Node('a');

// //      a

// console.log(howHigh(a)); // -> 0

//! TEST_04
// console.log(howHigh(null)); // -> -1
