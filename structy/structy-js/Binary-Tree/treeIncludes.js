// Write a function, treeIncludes, that takes in the root of a binary tree and a target value. The function should return a boolean indicating whether or not the value is contained in the tree.

class Node {
	constructor(val) {
		this.val = val;
		this.left = null;
		this.right = null;
	}
}

//!breadth
// const treeIncludes = (root, target) => {
// 	//edge case where root is null
// 	//set queue to first node
// 	//breadth transverse through tree and when equal to target set true
// 	if (root === null) return false;
// 	const queue = [root];
// 	const values = [];
// 	while (queue.length > 0) {
// 		const node = queue.shift();
// 		values.push(node.val);
// 		if (node.left !== null) queue.push(node.left);
// 		if (node.right !== null) queue.push(node.right);
// 	}
// 	return values.includes(target);
// };

//! alternate breadth
// const treeIncludes = (root, target) => {
// 	if (root === null) return false;
// 	const queue = [root];
// 	while (queue.length > 0) {
// 		const node = queue.shift();
// 		if (node.val === target) return true;
// 		if (node.left !== null) queue.push(node.left);
// 		if (node.right !== null) queue.push(node.right);
// 	}
// 	return false;
// };

//!depth / recursive
// const treeIncludes = (root, target) => {
//     if (root === null) return false;
//     if (root.val === target) return true;
//     return treeIncludes(root.left, target) || treeIncludes(root.right, target);
//   };


//! TEST_00
// const a = new Node('a');
// const b = new Node('b');
// const c = new Node('c');
// const d = new Node('d');
// const e = new Node('e');
// const f = new Node('f');

// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;

// //      a
// //    /   \
// //   b     c
// //  / \     \
// // d   e     f

// console.log(treeIncludes(a, 'e')); // -> true

//! TEST_01
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// const e = new Node("e");
// const f = new Node("f");

// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;

// //      a
// //    /   \
// //   b     c
// //  / \     \
// // d   e     f

// treeIncludes(a, "a"); // -> true

//! TEST_02
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// const e = new Node("e");
// const f = new Node("f");

// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;

// //      a
// //    /   \
// //   b     c
// //  / \     \
// // d   e     f

// treeIncludes(a, "n"); // -> false

//! TEST_03
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// const e = new Node("e");
// const f = new Node("f");
// const g = new Node("g");
// const h = new Node("h");

// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// f.right = h;

// //      a
// //    /   \
// //   b     c
// //  / \     \
// // d   e     f
// //    /       \
// //   g         h

// treeIncludes(a, "f"); // -> true

//! TEST_04
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// const e = new Node("e");
// const f = new Node("f");
// const g = new Node("g");
// const h = new Node("h");

// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// f.right = h;

// //      a
// //    /   \
// //   b     c
// //  / \     \
// // d   e     f
// //    /       \
// //   g         h

// treeIncludes(a, "p"); // -> false

//! TEST_05
// treeIncludes(null, "b"); // -> false
