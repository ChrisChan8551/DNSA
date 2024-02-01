// Write a function, breadthFirstValues, that takes in the root of a binary tree. The function should return an array containing all values of the tree in breadth-first order.
//

class Node {
	constructor(val) {
		this.val = val;
		this.left = null;
		this.right = null;
	}
}

const breadthFirstValues = (root) => {
	//queue instead of stack FIFO
	//left to right before going to next level
	if (root === null) return []; //edge case where root is empty or null
	const queue = [root]; //set queue to root node
	const values = [];
	while (queue.length > 0) {
		const node = queue.shift();
		values.push(node.val);
		if (node.left !== null) queue.push(node.left);
		if (node.right !== null) queue.push(node.right);
	}
	return values;
};

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

// breadthFirstValues(a);
// //    -> ['a', 'b', 'c', 'd', 'e', 'f']

//! TEST 01
// const a = new Node('a');
// const b = new Node('b');
// const c = new Node('c');
// const d = new Node('d');
// const e = new Node('e');
// const f = new Node('f');
// const g = new Node('g');
// const h = new Node('h');

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

// breadthFirstValues(a);
// //   -> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

// //! TEST 02
// const a = new Node('a');

// //      a

// breadthFirstValues(a);
// //    -> ['a']

//! TEST 03
// const a = new Node('a');
// const b = new Node('b');
// const c = new Node('c');
// const d = new Node('d');
// const e = new Node('e');
// const x = new Node('x');

// a.right = b;
// b.left = c;
// c.left = x;
// c.right = d;
// d.right = e;

// //      a
// //       \
// //        b
// //       /
// //      c
// //    /  \
// //   x    d
// //         \
// //          e

// breadthFirstValues(a);
// //    -> ['a', 'b', 'c', 'x', 'd', 'e']

//! TEST 04
// breadthFirstValues(null);
// //    -> []
