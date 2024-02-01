// linked list values
// Write a function, linkedListValues, that takes in the head of a linked list as an argument. The function should return an array containing all values of the nodes in the linked list.

// Hey. This is our first linked list problem, so you should be liberal with watching the Approach and Walkthrough. Be productive! -AZ

class Node {
	constructor(val) {
		this.val = val;
		this.next = null;
	}
}




//! iterative
const linkedListValues = (head) => {
	let current = head;
	let array = [];
	while (current != null) {
		array.push(current.val);
		current = current.next;
	}
	return array;
};

//! recursive
// const linkedListValues = (head) => {
//     const values = [];
//     _linkedListValues(head, values);
//     return values;
//   };

// const _linkedListValues = (head, values) => {
// 	if (head === null) return;
// 	values.push(head.val);
// 	_linkedListValues(head.next, values);
// };


const a = new Node('a');
const b = new Node('b');
const c = new Node('c');
const d = new Node('d');

a.next = b;
b.next = c;
c.next = d;

// a -> b -> c -> d

console.log(linkedListValues(a)); // -> [ 'a', 'b', 'c', 'd' ]

const x = new Node("x");
const y = new Node("y");

x.next = y;

// x -> y

console.log(linkedListValues(x)); // -> [ 'x', 'y' ]



const q = new Node("q");

// q

console.log(linkedListValues(q)); // -> [ 'q' ]
console.log(linkedListValues(null)); // -> [ ]
