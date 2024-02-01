// Write a function, treeMinValue, that takes in the root of a binary tree that contains number values. The function should return the minimum value within the tree.
// You may assume that the input tree is non-empty.

class Node {
	constructor(val) {
		this.val = val;
		this.left = null;
		this.right = null;
	}
}

//!breadth first
const treeMinValue = (root) => {
	const queue = [root]; //set queue to root node
	let min = root.val;
	while (queue.length > 0) {
		const node = queue.shift();
		if (node.val < min) {
			min = node.val;
		}
		if (node.left !== null) queue.push(node.left);
		if (node.right !== null) queue.push(node.right);
	}
	return min;
};

//! recursive
// const treeMinValue = (root) => {
//     if (root === null) return Infinity;
//     const smallestLeftValue = treeMinValue(root.left);
//     const smallestRightValue = treeMinValue(root.right);
//     return Math.min(root.val, smallestLeftValue, smallestRightValue);
//   };

//! depth first
// const treeMinValue = (root) => {
//     const stack = [root];

//     let smallest = Infinity;
//     while (stack.length) {
//       const current = stack.pop();
//       if (current.val < smallest) smallest = current.val;

//       if (current.left !== null) stack.push(current.left);
//       if (current.right !== null) stack.push(current.right);
//     }
//     return smallest;
//   };

//! TEST__00
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

console.log(treeMinValue(a)); // -> -2

//! TEST__01
// const a = new Node(5);
// const b = new Node(11);
// const c = new Node(3);
// const d = new Node(4);
// const e = new Node(14);
// const f = new Node(12);

// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;

// //       5
// //    /    \
// //   11     3
// //  / \      \
// // 4   14     12

// treeMinValue(a); // -> 3

//! TEST__02
// const a = new Node(-1);
// const b = new Node(-6);
// const c = new Node(-5);
// const d = new Node(-3);
// const e = new Node(-4);
// const f = new Node(-13);
// const g = new Node(-2);
// const h = new Node(-2);

// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// f.right = h;

// //        -1
// //      /   \
// //    -6    -5
// //   /  \     \
// // -3   -4   -13
// //     /       \
// //    -2       -2

// treeMinValue(a); // -> -13

//! TEST__03
// const a = new Node(42);

//    42

// treeMinValue(a); // -> 42
