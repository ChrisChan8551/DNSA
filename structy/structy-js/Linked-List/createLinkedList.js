// Write a function, createLinkedList, that takes in an array of values as an argument.
// The function should create a linked list containing each element of the array as the values of the nodes.
// The function should return the head of the linked list.

class Node {
	constructor(val) {
		this.val = val;
		this.next = null;
	}
}

const createLinkedList = (values) => {
	// interate through array of values
	// set first value as new node
	// if there's no values return null

	let head = new Node(null);
	let tail = head;
	for (let i = 0; i < values.length; i++) {
		tail.next = new Node(values[i]);
		tail = tail.next;
	}
	// return head.next;
	return head;
};

//! recursive
// const createLinkedList = (values, i = 0) => {
//     if (i === values.length) return null;
//     const head = new Node(values[i]);
//     head.next = createLinkedList(values, i + 1);
//     return head;
//   };

//! TEST 00
console.log(createLinkedList(['h', 'e', 'y']));
// h -> e -> y

//! TEST 01
// console.log(createLinkedList([1, 7, 1, 8]));
// 1 -> 7 -> 1 -> 8
//! TEST 02
// console.log(createLinkedList(['a']));
// a
//! TEST 03
// console.log(createLinkedList([]));
// null
