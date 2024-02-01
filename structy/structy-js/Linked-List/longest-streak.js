// Write a function, longestStreak, that takes in the head of a linked list as an argument. The function should return the length of the longest consecutive streak of the same value within the list.

class Node {
	constructor(val) {
		this.val = val;
		this.next = null;
	}
}

//tracking for max streak starting at 0
//track current streak if current streak is greater than max streak, then replace max streak with current streak
//

const longestStreak = (head) => {
	let current = head;
	let maxStreak = 0;
	let currentStreak = 0;
	let prev = null;

	while (current !== null) {
		// console.log('***current***: ', current.val);
		// console.log('***prev***: ', prev.val);
		//! prev cannot be prev.val. Prev is not a node
		if (current.val === prev) {
			currentStreak += 1;
		} else {
			currentStreak = 1;
		}
		if (currentStreak > maxStreak) {
			maxStreak = currentStreak;
		}
		prev = current.val;
		current = current.next;
	}
	return maxStreak;
};

//!test_00
// const a = new Node(5);
// const b = new Node(5);
// const c = new Node(7);
// const d = new Node(7);
// const e = new Node(7);
// const f = new Node(6);

// a.next = b;
// b.next = c;
// c.next = d;
// d.next = e;
// e.next = f;

// 5 -> 5 -> 7 -> 7 -> 7 -> 6

// console.log(longestStreak(a)); // 3

//!test_01
const a = new Node(3);
const b = new Node(3);
const c = new Node(3);
const d = new Node(3);
const e = new Node(9);
const f = new Node(9);

a.next = b;
b.next = c;
c.next = d;
d.next = e;
e.next = f;

// 3 -> 3 -> 3 -> 3 -> 9 -> 9

console.log(longestStreak(a)); // 4

//!test_02
// const a = new Node(9);
// const b = new Node(9);
// const c = new Node(1);
// const d = new Node(9);
// const e = new Node(9);
// const f = new Node(9);

// a.next = b;
// b.next = c;
// c.next = d;
// d.next = e;
// e.next = f;

// // 9 -> 9 -> 1 -> 9 -> 9 -> 9

// console.log(longestStreak(a)); // 3

// //test_03
// const a = new Node(5);
// const b = new Node(5);

// a.next = b;

// // 5 -> 5

// console.log(longestStreak(a)); // 2

// //test_04
// const a = new Node(4);

// // 4

// console.log(longestStreak(a)); // 1

// //test_05
// console.log(longestStreak(null)); // 0
