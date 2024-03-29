// Write a function, treeValueCount, that takes in the root of a binary tree and a target value. The function should return the number of times that the target occurs in the tree.

class Node {
	constructor(val) {
		this.val = val;
		this.left = null;
		this.right = null;
	}
}

const treeValueCount = (root, target) => {
	// edge case - if tree / root is null return 0
	if (root === null) return 0;

	let count = 0;
	let queue = [root];
	// transvers through the tree and count each node with target value.
	while (queue.length > 0) {
		const node = queue.shift();
		// console.log(node.val);
		if (node.val === target) count++;
		if (node.left !== null) queue.push(node.left);
		if (node.right !== null) queue.push(node.right);
	}
	return count;
};

//! TEST_00
const a = new Node(12);
const b = new Node(6);
const c = new Node(6);
const d = new Node(4);
const e = new Node(6);
const f = new Node(12);

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;

//      12
//    /   \
//   6     6
//  / \     \
// 4   6     12

console.log(treeValueCount(a, 6)); // -> 3

//! TEST_01
//   const a = new Node(12);
// const b = new Node(6);
// const c = new Node(6);
// const d = new Node(4);
// const e = new Node(6);
// const f = new Node(12);

// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;

// //      12
// //    /   \
// //   6     6
// //  / \     \
// // 4  6     12

// treeValueCount(a,  12); // -> 2

//! TEST_02
//   const a = new Node(7);
// const b = new Node(5);
// const c = new Node(1);
// const d = new Node(1);
// const e = new Node(8);
// const f = new Node(7);
// const g = new Node(1);
// const h = new Node(1);

// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// f.right = h;

// //      7
// //    /   \
// //   5     1
// //  / \     \
// // 1   8     7
// //    /       \
// //   1         1
// treeValueCount(a, 1); // -> 4

//! TEST_03
//   const a = new Node(7);
// const b = new Node(5);
// const c = new Node(1);
// const d = new Node(1);
// const e = new Node(8);
// const f = new Node(7);
// const g = new Node(1);
// const h = new Node(1);

// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// f.right = h;

// //      7
// //    /   \
// //   5     1
// //  / \     \
// // 1   8     7
// //    /       \
// //   1         1

// treeValueCount(a, 9); // -> 0

//! TEST_04
//   treeValueCount(null, 42); // -> 0
