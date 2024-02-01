// Write a function, maxPathSum, that takes in the root of a binary tree that contains number values. The function should return the maximum sum of any root to leaf path within the tree.

// You may assume that the input tree is non-empty.

class Node {
	constructor(val) {
		this.val = val;
		this.left = null;
		this.right = null;
	}
}

//! recursive solution works best for this problem.
// const maxPathSum = (root) => {
// 	if (root === null) return -Infinity;
// 	if (root.left === null && root.right === null) return root.val;
// 	return root.val + Math.max(maxPathSum(root.left), maxPathSum(root.right));
// };

//!interative solution is really long.

const maxPathSum = (root) => {
	let maxSum = -Infinity;
	const stack = [];
	const visited = new Set();
	let current = root;
	let lastVisited = null;
	let currentSum = 0;

	while (stack.length > 0 || current) {
		if (current) {
			stack.push(current);
			currentSum += current.val;
			current = current.left;
		} else {
			const peekNode = stack[stack.length - 1];

			if (
				peekNode.right &&
				lastVisited !== peekNode.right &&
				!visited.has(peekNode.right)
			) {
				current = peekNode.right;
			} else {
				if (!peekNode.left && !peekNode.right) {
					maxSum = Math.max(maxSum, currentSum);
				}
				lastVisited = stack.pop();
				visited.add(lastVisited);
				currentSum -= lastVisited.val;
			}
		}
	}

	return maxSum;
};

//! TEST_00
// const a = new Node(3);
// const b = new Node(11);
// const c = new Node(4);
// const d = new Node(4);
// const e = new Node(-2);
// const f = new Node(1);

// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;

// //       3
// //    /    \
// //   11     4
// //  / \      \
// // 4   -2     1

// maxPathSum(a); // -> 18

//! TEST_01
// const a = new Node(5);
// const b = new Node(11);
// const c = new Node(54);
// const d = new Node(20);
// const e = new Node(15);
// const f = new Node(1);
// const g = new Node(3);

// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// e.left = f;
// e.right = g;

// //        5
// //     /    \
// //    11    54
// //  /   \
// // 20   15
// //      / \
// //     1  3

// maxPathSum(a); // -> 59

//! TEST_02
// const a = new Node(-1);
// const b = new Node(-6);
// const c = new Node(-5);
// const d = new Node(-3);
// const e = new Node(0);
// const f = new Node(-13);
// const g = new Node(-1);
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
// // -3   0    -13
// //     /       \
// //    -1       -2

// maxPathSum(a); // -> -8

//! TEST_03
// const a = new Node(42);

// //        42

// maxPathSum(a); // -> 42
