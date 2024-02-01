// Write a function, pathFinder, that takes in the root of a binary tree and a target value. The function should return an array representing a path to the target value. If the target value is not found in the tree, then return null.

// You may assume that the tree contains unique values.

class Node {
	constructor(val) {
		this.val = val;
		this.left = null;
		this.right = null;
	}
}

//! depth first = Time: O(n^2)
// const pathFinder = (root, target) => {
// 	// return array of paths if value meets target.
// 	//base case if root is null and when value = target
// 	if (root === null) return null; // return null if root is null
// 	if (root.val === target) return [root.val]; //if root is the target, then just return array of the root.val
// 	//if you stuck finding a solution, start with writing the recursive function
// 	// pathFinder(root.left,target)

// 	// pathFinder(root.right,target)
// 	// check if left and right are not null
// 	const leftPath = pathFinder(root.left, target);
// 	if (leftPath !== null) return [root.val, ...leftPath];
// 	const rightPath = pathFinder(root.right, target);
// 	if (rightPath !== null) return [root.val, ...rightPath];

// 	return null; //return null if target is not found
// };

//! depth first w/ push - Time: O(n)
const pathFinder = (root, target) => {
	const result = pathFinderHelper(root, target);
	if (result === null) {
	  return null;
	} else {
	  return result.reverse();
	}
  };

  const pathFinderHelper = (root, target) => {
	if (root === null) return null;
	if (root.val === target) return [ root.val ];

	const leftPath = pathFinderHelper(root.left, target);
	if (leftPath !== null) {
	  leftPath.push(root.val);
	  return leftPath;
	}

	const rightPath = pathFinderHelper(root.right, target);
	if (rightPath !== null) {
	  rightPath.push(root.val);
	  return rightPath;
	}

	return null;
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

console.log(pathFinder(a, 'e')); // -> [ 'a', 'b', 'e' ]

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

// pathFinder(a, 'p'); // -> null

//! TEST_02
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

// pathFinder(a, "c"); // -> ['a', 'c']

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

// pathFinder(a, "h"); // -> ['a', 'c', 'f', 'h']

//! TEST_04
// const x = new Node("x");

// //      x

// pathFinder(x, "x"); // -> ['x']

//! TEST_05
// pathFinder(null, "x"); // -> null

//! TEST_06
// const root = new Node(0);
// let curr = root;
// for (let i = 1; i <= 6000; i += 1) {
//   curr.right = new Node(i);
//   curr = curr.right;
// }

// //      0
// //       \
// //        1
// //         \
// //          2
// //           \
// //            3
// //             .
// //              .
// //               .
// //              5999
// //                \
// //                6000

// pathFinder(root, 3451); // -> [0, 1, 2, 3, ..., 3450, 3451]
