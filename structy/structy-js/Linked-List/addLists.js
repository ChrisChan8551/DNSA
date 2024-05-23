// Write a function, addLists, that takes in the 1 of two linked lists, each representing a number. The nodes of the linked lists contain digits as values. The nodes in the input lists are reversed; this means that the least significant digit of the number is the head. The function should return the head of a new linked listed representing the sum of the input lists. The output list should have its digits reversed as well.

// You must do this by traversing through the linked lists once.
// Say we wanted to compute 621 + 354 normally. The sum is 975:

//    621
//  + 354
//  -----
//    975

// Then, the reversed linked list format of this problem would appear as:

//     1 -> 2 -> 6
//  +  4 -> 5 -> 3
//  --------------
//     5 -> 7 -> 9

class Node {
	constructor(val) {
		this.val = val;
		this.next = null;
	}
}

// const addLists = (head1, head2) => {
	//1) transverse both lists in reverse order
	//2) sum both lists in reverse order
	//3) null = 0
	//4) handle a carry digit
	//5) handle final carry digit

// };

//! recursive
const addLists = (head1, head2, carry = 0) => {
	if (head1 === null && head2 === null && carry === 0) return null;
	const val1 = head1 === null ? 0 : head1.val;
	const val2 = head2 === null ? 0 : head2.val;

	const sum = val1 + val2 + carry;
	const nextCarry = sum > 9 ? 1 : 0;
	const digit = sum % 10;

	const result = new Node(digit);

	const next1 = head1 === null ? null : head1.next;
	const next2 = head2 === null ? null : head2.next;

	result.next = addLists(next1, next2, nextCarry);
	return result;
};

//! TEST 00
//   621
// + 354
// -----
//   975

const a1 = new Node(1);
const a2 = new Node(2);
const a3 = new Node(6);
a1.next = a2;
a2.next = a3;
// 1 -> 2 -> 6

const b1 = new Node(4);
const b2 = new Node(5);
const b3 = new Node(3);
b1.next = b2;
b2.next = b3;
// 4 -> 5 -> 3

console.log(addLists(a1, b1));
// 5 -> 7 -> 9

//! TEST 01
// //  7541
// // +  32
// // -----
// //  7573

// const a1 = new Node(1);
// const a2 = new Node(4);
// const a3 = new Node(5);
// const a4 = new Node(7);
// a1.next = a2;
// a2.next = a3;
// a3.next = a4;
// // 1 -> 4 -> 5 -> 7

// const b1 = new Node(2);
// const b2 = new Node(3);
// b1.next = b2;
// // 2 -> 3

// console.log(addLists(a1, b1));
// // 3 -> 7 -> 5 -> 7

//! TEST 02
// //   39
// // + 47
// // ----
// //   86

// const a1 = new Node(9);
// const a2 = new Node(3);
// a1.next = a2;
// // 9 -> 3

// const b1 = new Node(7);
// const b2 = new Node(4);
// b1.next = b2;
// // 7 -> 4

// addLists(a1, b1);
// // 6 -> 8

//! TEST 03
// //   89
// // + 47
// // ----
// //  136

// const a1 = new Node(9);
// const a2 = new Node(8);
// a1.next = a2;
// // 9 -> 8

// const b1 = new Node(7);
// const b2 = new Node(4);
// b1.next = b2;
// // 7 -> 4

// addLists(a1, b1);
// // 6 -> 3 -> 1

//! TEST 04
// //   999
// //  +  6
// //  ----
// //  1005

// const a1 = new Node(9);
// const a2 = new Node(9);
// const a3 = new Node(9);
// a1.next = a2;
// a2.next = a3;
// // 9 -> 9 -> 9

// const b1 = new Node(6);
// // 6

// addLists(a1, b1);
// // 5 -> 0 -> 0 -> 1
