// Write a function, allTreePaths, that takes in the root of a binary tree. The function should return a 2-Dimensional array where each subarray represents a root-to-leaf path in the tree.

// The order within an individual path must start at the root and end at the leaf, but the relative order among paths in the outer array does not matter.

// You may assume that the input tree is non-empty.

class Node {
	constructor(val) {
		this.val = val;
		this.left = null;
		this.right = null;
	}
}

const allTreePaths = (root) => {
	if (root === null) return []; //base case
	if (root.left === null && root.right === null) return [[root.val]]; //if there is only root node, and it is said that paths need to be subarrays, thus root.val is another array.

	const paths = [];

	const leftSubPaths = allTreePaths(root.left);
	for (let subPath of leftSubPaths) {
		paths.push([root.val, ...subPath]); // spread operator creates a copy of the array and concatenates multiple arrays together
	}

	const rightSubPaths = allTreePaths(root.right);
	for (let subPath of rightSubPaths) {
		paths.push([root.val, ...subPath]); // spread operator creates a copy of the array and concatenates multiple arrays together
	}

	return paths;
};

//! alternate iterative solution
// const allTreePaths = (root) => {
// 	// Initialize an empty array to store the result paths.
// 	const paths = [];

// 	// Initialize a stack to keep track of the current path.
// 	const stack = [];

// 	// Initialize the stack with the root node and an empty path.
// 	stack.push([root, []]);

// 	// While there are nodes in the stack to explore,
// 	while (stack.length > 0) {
// 		const [currentNode, currentPath] = stack.pop();

// 		// If the current node is a leaf node, add the path to the result.
// 		if (!currentNode.left && !currentNode.right) {
// 			paths.push([...currentPath, currentNode.val]);
// 		}

// 		// If there's a right child, push it onto the stack with the updated path.
// 		if (currentNode.right) {
// 			stack.push([currentNode.right, [...currentPath, currentNode.val]]);
// 		}

// 		// If there's a left child, push it onto the stack with the updated path.
// 		if (currentNode.left) {
// 			stack.push([currentNode.left, [...currentPath, currentNode.val]]);
// 		}
// 	}

// 	return paths;
// };

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

console.log(allTreePaths(a)); // ->
// [
//   [ 'a', 'b', 'd' ],
//   [ 'a', 'b', 'e' ],
//   [ 'a', 'c', 'f' ]
// ]

//! TEST_01
// const a = new Node('a');
// const b = new Node('b');
// const c = new Node('c');
// const d = new Node('d');
// const e = new Node('e');
// const f = new Node('f');
// const g = new Node('g');
// const h = new Node('h');
// const i = new Node('i');

// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// e.right = h;
// f.left = i;

// //         a
// //      /    \
// //     b      c
// //   /  \      \
// //  d    e      f
// //      / \    /
// //     g  h   i

// allTreePaths(a); // ->
// // [
// //   [ 'a', 'b', 'd' ],
// //   [ 'a', 'b', 'e', 'g' ],
// //   [ 'a', 'b', 'e', 'h' ],
// //   [ 'a', 'c', 'f', 'i' ]
// // ]

//! TEST_02
// const q = new Node('q');
// const r = new Node('r');
// const s = new Node('s');
// const t = new Node('t');
// const u = new Node('u');
// const v = new Node('v');

// q.left = r;
// q.right = s;
// r.right = t;
// t.left = u;
// u.right = v;

// //      q
// //    /   \
// //   r     s
// //    \
// //     t
// //    /
// //   u
// //  /
// // v

// allTreePaths(q); // ->
// // [
// //   [ 'q', 'r', 't', 'u', 'v' ],
// //   [ 'q', 's' ]
// // ]

//! TEST_03
// const z = new Node('z');

// //      z

// allTreePaths(z); // ->
// // [
// //   ['z']
// // ]
