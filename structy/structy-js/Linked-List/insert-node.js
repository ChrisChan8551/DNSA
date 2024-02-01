// Write a function, insertNode, that takes in the head of a linked list, a value, and an index. The function should insert a new node with the value into the list at the specified index. Consider the head of the linked list as index 0. The function should return the head of the resulting linked list.

// Do this in-place.

// You may assume that the input list is non-empty and the index is not greater than the length of the input list.

class Node {
	constructor(val) {
		this.val = val;
		this.next = null;
	}
}

const insertNode = (head, value, index) => {
	// set up count variable
	// edge case
	// if there's no linked list then start at head or return the head
	// if index is greater than length of linked list then insert at the tail
	// insert at index 0 - need to explicitly set new head to value then new head.next to the head

	if (index === 0) {
		newHead = new Node(value);
		newHead.next = head;
		return newHead;
	}

	let current = head;
	let count = 0;

	while (current !== null) {
		// transverse the linked list
		// if count is index-1 then create new node and set it to current.next;
		if (count === index - 1) {
			let next = current.next;
			current.next = new Node(value);
			current.next.next = next;
		}
		count++;
		current = current.next;
	}

	return head;
};

//! TEST 00
// const a = new Node('a');
// const b = new Node('b');
// const c = new Node('c');
// const d = new Node('d');

// a.next = b;
// b.next = c;
// c.next = d;

// // // a -> b -> c -> d

// insertNode(a, 'x', 2);
// // a -> b -> x -> c -> d

//! TEST 01
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");

// a.next = b;
// b.next = c;
// c.next = d;

// // a -> b -> c -> d

// insertNode(a, 'v', 3);
// // a -> b -> c -> v -> d

//! TEST 02
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");

// a.next = b;
// b.next = c;
// c.next = d;

// // a -> b -> c -> d

// insertNode(a, 'm', 4);
// // a -> b -> c -> d -> m

//! TEST 03
// const a = new Node("a");
// const b = new Node("b");

// a.next = b;

// // a -> b

// console.log(insertNode(a, 'z', 0));
// // z -> a -> b
