// is univalue list
// Write a function, isUnivalueList, that takes in the head of a linked list as an argument. The function should return a boolean indicating whether or not the linked list contains exactly one unique value.

// You may assume that the input list is non-empty.

class Node {
	constructor(val) {
		this.val = val;
		this.next = null;
	}
}
//! iterative
// const isUnivalueList = (head) => {
// 	let current = head;
// 	while (current !== null) {
// 		if (current.val !== head.val) return false;
// 		else {
// 			current = current.next;
// 		}
// 	}
// 	return true;
// };

//! recursive
const isUnivalueList = (head, prev = null) => {
	if (head === null) return true;
	if (prevVal === null || prevVal === head.val) {
		return isUnivalueList(head.next, head.val);
	} else {
		return false;
	}
};

//test 0
// const a = new Node(7);
// const b = new Node(7);
// const c = new Node(7);

// a.next = b;
// b.next = c;

// // 7 -> 7 -> 7

// isUnivalueList(a); // true

// //test 1
// const a = new Node(7);
// const b = new Node(7);
// const c = new Node(4);

// a.next = b;
// b.next = c;

// // 7 -> 7 -> 4

// isUnivalueList(a); // false

// // test 2
// const u = new Node(2);
// const v = new Node(2);
// const w = new Node(2);
// const x = new Node(2);
// const y = new Node(2);

// u.next = v;
// v.next = w;
// w.next = x;
// x.next = y;

// // 2 -> 2 -> 2 -> 2 -> 2

// isUnivalueList(u); // true

// //test 3
// const u = new Node(2);
// const v = new Node(2);
// const w = new Node(3);
// const x = new Node(3);
// const y = new Node(2);

// u.next = v;
// v.next = w;
// w.next = x;
// x.next = y;

// // 2 -> 2 -> 3 -> 3 -> 2

// isUnivalueList(u); // false

// //test 4
// const z = new Node('z');

// // z

// isUnivalueList(z); // true
