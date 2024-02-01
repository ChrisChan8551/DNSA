// Write a function, depthFirstValues, that takes in the root of a binary tree. The function should return an array containing all values of the tree in depth-first order.

// Hey. This is our first binary tree problem, so be extra sure to check out the approach video! -AZ

class Node {
	constructor(val) {
		this.val = val;
		this.left = null;
		this.right = null;
	}
}

const depthFirstValues = (root) => {
	// todo
	// take in root node
	// if root is doesn't have left and right child = set null
	if (root === null) return []; //edge case when tree is empty
	const stack = [root]; // start stack with root node
	const result = []; // set variable for array of values

	while (stack.length > 0) {
		const node = stack.pop();
		result.push(node.val);

		if (node.right !== null) stack.push(node.right);
		if (node.left !== null) stack.push(node.left);
	}

	return result;
};

//! recursive
// const depthFirstValues = (root) => {
// 	if (root === null)
// 	  return [];

// 	const leftValues = depthFirstValues(root.left);
// 	const rightValues = depthFirstValues(root.right);
// 	return [ root.val, ...leftValues, ...rightValues ];
//   };

//! TEST 00
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

// depthFirstValues(a);
// //    -> ['a', 'b', 'd', 'e', 'c', 'f']

//! TEST 01
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
// e.left = g;

// //      a
// //    /   \
// //   b     c
// //  / \     \
// // d   e     f
// //    /
// //   g

// depthFirstValues(a);
// //    -> ['a', 'b', 'd', 'e', 'g', 'c', 'f']

//! TEST 02
// const a = new Node('a');
// //      a
// depthFirstValues(a);
// //    -> ['a']

//! TEST 03
// const a = new Node('a');
// const b = new Node('b');
// const c = new Node('c');
// const d = new Node('d');
// const e = new Node('e');

// a.right = b;
// b.left = c;
// c.right = d;
// d.right = e;

// //      a
// //       \
// //        b
// //       /
// //      c
// //       \
// //        d
// //         \
// //          e

// depthFirstValues(a);
// //    -> ['a', 'b', 'c', 'd', 'e']

//! TEST 04
depthFirstValues(null);
//    -> []
