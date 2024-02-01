// Write a function, removeNode, that takes in the head of a linked list and a target value as arguments. The function should delete the node containing the target value from the linked list and return the head of the resulting linked list. If the target appears multiple times in the linked list, only remove the first instance of the target in the list.

// Do this in-place.

// You may assume that the input list is non-empty.

// You may assume that the input list contains the target.

class Node {
	constructor(val) {
		this.val = val;
		this.next = null;
	}
}

// const removeNode = (head, targetVal) => {
// 	let current = head;
// 	let prev = null;

// 	//edge case if head = target value. return head.next
// 	if (head.val == targetVal) return head.next;

// 	while (current !== null) {
// 		//transverse the linked list and look for target value

// 		if (current.val == targetVal) {
// 			//if the current node = target value, point previous.next to current.next;
// 			prev.next = current.next;
// 			break;
// 		}

// 		prev = current;
// 		current = current.next;
// 	}
// 	//if nothing matches then return the head.

// 	return head;
// };

//! recursive
// const removeNode = (head, targetVal) => {
// 	if (head === null) return null;
// 	if (head.val === targetVal) return head.next;
// 	head.next = removeNode(head.next, targetVal);
// 	return head;
// };

//! Test_00
const a = new Node('a');
const b = new Node('b');
const c = new Node('c');
const d = new Node('d');
const e = new Node('e');
const f = new Node('f');

a.next = b;
b.next = c;
c.next = d;
d.next = e;
e.next = f;

// a -> b -> c -> d -> e -> f

console.log(removeNode(a, 'c'));
// // a -> b -> d -> e -> f

//! Test_01
// const x = new Node("x");
// const y = new Node("y");
// const z = new Node("z");

// x.next = y;
// y.next = z;

// // x -> y -> z

// removeNode(x, "z");
// // x -> y

//! Test_02
// const q = new Node("q");
// const r = new Node("r");
// const s = new Node("s");

// q.next = r;
// r.next = s;

// // q -> r -> s

// removeNode(q, "q");
// // r -> s

//! Test_03
// const node1 = new Node("h");
// const node2 = new Node("i");
// const node3 = new Node("j");
// const node4 = new Node("i");

// node1.next = node2;
// node2.next = node3;
// node3.next = node4;

// // h -> i -> j -> i

// removeNode(node1, "i");
// // h -> j -> i

//! Test_04
// const t = new Node("t");

// // t

// removeNode(t, "t");
// // null
