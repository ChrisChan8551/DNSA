// Write a function, compress, that takes in a string as an argument. The function should return a compressed version of the string where consecutive occurrences of the same characters are compressed into the number of occurrences followed by the character. Single character occurrences should not be changed.

// 'aaa' compresses to '3a'
// 'cc' compresses to '2c'
// 't' should remain as 't'
// You can assume that the input only contains alphabetic characters.

const compress = (s) => {
	let result = [];
	let i = 0;
	let j = 0;

	while (j <= s.length) {
		if (s[i] === s[j]) {
			j += 1;
		} else {
			const num = j - i;
			if (num === 1) {
				result.push(s[i]);
			} else {
				result.push(String(num), s[i]);
			}
			i = j;
		}
	}

	return result.join('');
};

// !TEST_00
// compress('ccaaatsss'); // -> '2c3at3s'

// !TEST_01
// compress('ssssbbz'); // -> '4s2bz'

// !TEST_02
// compress('ppoppppp'); // -> '2po5p'

// !TEST_03
// compress('nnneeeeeeeeeeeezz'); // -> '3n12e2z'

// !TEST_04
// compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy');
// // -> '127y'
