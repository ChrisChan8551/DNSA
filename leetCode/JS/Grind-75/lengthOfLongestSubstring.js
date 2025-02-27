// Given a string s, find the length of the longest
// substring
//  without repeating characters.

// Example 1:

// Input: s = "abcabcbb"
// Output: 3
// Explanation: The answer is "abc", with the length of 3.
// Example 2:

// Input: s = "bbbbb"
// Output: 1
// Explanation: The answer is "b", with the length of 1.
// Example 3:

// Input: s = "pwwkew"
// Output: 3
// Explanation: The answer is "wke", with the length of 3.
// Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

// Constraints:

// 0 <= s.length <= 5 * 104
// s consists of English letters, digits, symbols and spaces.

// const lengthOfLongestSubstring = function (s) {
// 	let letters = new Set();
// 	let i = 0;
// 	let j = 0;
// 	let max = 0;
// 	while (i < s.length && j < s.length) {
// 		if (!letters.has(s[j])) {
// 			letters.add(s[j]);
// 			max = Math.max(max, j - i + 1); // compare max length with current max length, replace maxLength if current is greater
// 			j++;
// 		} else {
// 			letters.delete(s[i]); // reset if letters start matching
// 			i++;
// 		}
// 	}

// 	return max;
// };

const lengthOfLongestSubstring = function (s) {
	let maxLength = 0;
	let start = 0;
	let charSet = new Set();
	for (let end = 0; end < s.length; end++) {
		let char = s[end];
		while (charSet.has(char)) {
			charSet.delete(s[start]);
			start++;
		}
		charSet.add(char);
		maxLength = Math.max(maxLength, end - start + 1);
	}
};
console.log(lengthOfLongestSubstring('abcabcbb'));
// console.log(lengthOfLongestSubstring('bbbbb'));
// console.log(lengthOfLongestSubstring('pwwkew'));
