// Write a function, treeSum, that takes in the root of a binary tree that contains number values. The function should return the total sum of all values in the tree.

class Node {
	constructor(val) {
		this.val = val;
		this.left = null;
		this.right = null;
	}
}

const treeSum = (root) => {
	if (root === null) return 0; //edge case if tree is empty
	let sum = 0; // set variable for sum
	let queue = [root];

	while (queue.length > 0) {
		const node = queue.shift();
		sum += node.val;

		if (node.left !== null) queue.push(node.left);
		if (node.right !== null) queue.push(node.right);
	}
	return sum;
};

//! TEST 00
const a = new Node(3);
const b = new Node(11);
const c = new Node(4);
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
//   11     4
//  / \      \
// 4   -2     1

console.log(treeSum(a)); // -> 21

//! TEST 01
// const a = new Node(1);
// const b = new Node(6);
// const c = new Node(0);
// const d = new Node(3);
// const e = new Node(-6);
// const f = new Node(2);
// const g = new Node(2);
// const h = new Node(2);

// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// f.right = h;

// //      1
// //    /   \
// //   6     0
// //  / \     \
// // 3   -6    2
// //    /       \
// //   2         2

// treeSum(a); // -> 10

//! TEST 02
// treeSum(null); // -> 0
