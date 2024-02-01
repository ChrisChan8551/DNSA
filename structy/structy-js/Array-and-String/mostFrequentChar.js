// most frequent char
// Write a function, mostFrequentChar, that takes in a string as an argument. The function should return the most frequent character of the string. If there are ties, return the character that appears earlier in the string.

// You can assume that the input string is non-empty.


const mostFrequentChar = (s) => {
	const count = {};

	for (let char of s) {
		// console.log(char);
		if (char in count) {
			count[char]++;
		} else {
			count[char] = 1;
		}
		// console.log(count);
	}

	let best;
	for (let char of s) {
		// console.log('value: ', count[char]);
		// console.log('best: ', best);
		if (!best || count[best] < count[char]) {
			best = char;
		}
	}

	return best;
};

console.log(mostFrequentChar('bookeeper')); // -> 'e'
console.log(mostFrequentChar('david')); // -> 'd'
console.log(mostFrequentChar('abby')); // -> 'b'
console.log(mostFrequentChar('mississippi')); // -> 'i'
console.log(mostFrequentChar('potato')); // -> 'o'
console.log(mostFrequentChar('eleventennine')); // -> 'e'
console.log(mostFrequentChar('riverbed')); // -> 'r'
