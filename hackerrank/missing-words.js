// Given a string s, and a substring t, where s and t are both space separated string sequences of words, and all words of t are definitely contained in s, return the ordered sequence of words in s that do not appear in the t subsequence as a list of those strings.

// For example if our two inputs s, and t are

// s = "I went to school last week and ate a super super carne asada burrito afterwards for dinner"

// t = "went last week and ate a super burrito for dinner"

// The expected output of the function would be
// ["I", "to", "school", "super, "carne", "asada", "afterwards"] (note only one "super" in the result)

const missingWords = (s, t) => {
	let sWords = s.split(' ');
	let tWords = t.split(' ');
	let result = [];
	let removed = [];
	// console.log(tWords);
	for (word of sWords) {
		if (tWords.includes(word) && !removed.includes(word)) {
			removed.push(word);
		} else {
			result.push(word);
		}
	}
	return result.join(' ');
};
const s =
	'I went to school last week and ate a super super carne asada burrito afterwards for dinner';
const t = 'went last week and ate a super burrito for dinner';

console.log(missingWords(s, t));
