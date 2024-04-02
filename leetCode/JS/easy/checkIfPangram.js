// https://leetcode.com/problems/check-if-the-sentence-is-pangram/

// A pangram is a sentence where every letter of the English alphabet appears at least once.

// Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

//! Example 1:
// Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
// Output: true
// Explanation: sentence contains at least one of every letter of the English alphabet.

//! Example 2:
// Input: sentence = "leetcode"
// Output: false


// Constraints:

// 1 <= sentence.length <= 1000
// sentence consists of lowercase English letters.

const checkIfPangram = (sentence) => {
    if (sentence.length < 26) {
        return false
    }

    let character = {}
    let alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for (let char of alphabet) {
        character[char] = 1
    }
    for (let char in sentence) {
        if (character[char]) {
            character[char] -= 1
        }
    }
    for (let key in character) {
        if (character[key] === 1) {
            return false
        }
    }
    return true
}

//! Example 1:
sentence = "thequickbrownfoxjumpsoverthelazydog"
console.log(checkIfPangram(sentence))
// Output: true
// Explanation: sentence contains at least one of every letter of the English alphabet.

//! Example 2:
sentence = "leetcode"
console.log(checkIfPangram(sentence))
// Output: false
