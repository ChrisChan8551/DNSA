// you are given a string of encrypted text
// (ciphertext)
// The encryption algorithm used to create the ciphertext simply shifts all the alphabetic characters in the original (unencrypted) string by the same amount. But you don't know what this amount is
// Write the decipher function that takes the encrypted function that takes the encrypted string as input, and returns the original, unencrypted string.

// For example, imagine that the original message was 'hello', and we shifted each letter by two.
// The resulting ciphertext would be 'jgnnq'.

// if the original message were "Coding tests are fun and challenging!" and we shifted each character by two, the resulting ciphertext would be 'Eqfkpi vguvu ctg hwp cpf ejcnngpikpi!'

// the decipher function takes two arguments: the ciphertext, and a word that we know appeared in the original plain text. using these clues, the function must output the original text.


// We will follow the English alphabet for this question. Note that the last letter of the alphabet Z will be followed by A. Likewise, z will be followed by a.
// If the word you are searching for in th eorignal string does not appear there, return 'Invalid'.

// ! Example 1
// let input ='Eqfkpi vguvu ctg hwp!'
// let original = 'tests'

// output:
// 'Coding tests are fun!'
// Explanation:
// 'tests' is a five-letter word. In the encrypted string, the only five-lette work is 'vguvu'. Therefore the encrypted version of 'tests' may be 'vguvu'
// On comparing 'tests' to 'vguvu', it i s clear that the encryption process has shifted every character in the plaintext by 2. So, the plaintext in this case is 'Coding tests are fun!'.

// ! Example 2
// let input = 'cdeb nqxcg'
// let original = 'love'

// Output:
// 'abcz love'

// Explanation:
// In this case, 'love' could have been encrypted to either 'cdeb' or 'nqxg' On closer examination, it is clear that 'nqxg' is the correct option, with every character shifted by 2.
// (No such relationship exists between 'love' and 'cdeb')


// const decipher = (encrypted, original) => {


// }

// ! Example 1
// let input ='Eqfkpi vguvu ctg hwp!'
// let original = 'tests'

// output:
// 'Coding tests are fun!'
// Explanation:
// 'tests' is a five-letter word. In the encrypted string, the only five-lette work is 'vguvu'. Therefore the encrypted version of 'tests' may be 'vguvu'
// On comparing 'tests' to 'vguvu', it i s clear that the encryption process has shifted every character in the plaintext by 2. So, the plaintext in this case is 'Coding tests are fun!'.

// ! Example 2
// let input = 'cdeb nqxcg'
// let original = 'love'

// Output:
// 'abcz love'

// Explanation:
// In this case, 'love' could have been encrypted to either 'cdeb' or 'nqxg' On closer examination, it is clear that 'nqxg' is the correct option, with every character shifted by 2.
// (No such relationship exists between 'love' and 'cdeb')
