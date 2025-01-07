var lengthOfLongestSubstring = function (s) {
	let unique = new Set();
	let start = 0;
	let max = 0;
	for (let i = 0; i < s.length; i++) {
		while (unique.has(s[i])) {
			unique.delete(s[start]);
			start++;
		}
		unique.add(s[i]);
        max = Math.max(max, i - start + 1);
	}
	return max;
};

console.log(lengthOfLongestSubstring('abcabcbb')); //3
console.log(lengthOfLongestSubstring('bbbbb')); // 1
console.log(lengthOfLongestSubstring('pwwkew')); // 3
