// https://leetcode.com/problems/count-good-triplets/


// Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

// A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

// 0 <= i < j < k < arr.length
// |arr[i] - arr[j]| <= a
// |arr[j] - arr[k]| <= b
// |arr[i] - arr[k]| <= c
// Where |x| denotes the absolute value of x.

// Return the number of good triplets.

//! Example 1:
// Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
// Output: 4
// Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].

//! Example 2:
// Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1
// Output: 0
// Explanation: No triplet satisfies all conditions.


// Constraints:

// 3 <= arr.length <= 100
// 0 <= arr[i] <= 1000
// 0 <= a, b, c <= 1000

const countGoodTriplets = function (arr, a, b, c) {
    // Get the length of the input array
    const n = arr.length;
    // Initialize a variable to store the count of good triplets
    let count = 0;
    // Iterate over the array to find the first element of the triplet
    for (let i = 0; i < n; i++) {
        // Iterate over the array to find the second element of the triplet
        for (let j = i + 1; j < n; j++) {
            // Check if the absolute difference between the first and second elements
            // satisfies the condition specified by 'a'
            if (Math.abs(arr[i] - arr[j]) <= a) {
                // If the condition is satisfied, iterate over the array to find the third element of the triplet
                for (let k = j + 1; k < n; k++) {
                    // Check if the absolute differences between the second and third elements,
                    // and between the first and third elements, satisfy the conditions specified by 'b' and 'c' respectively
                    if (Math.abs(arr[j] - arr[k]) <= b && Math.abs(arr[i] - arr[k]) <= c) {
                        // If all conditions are satisfied, increment the count of good triplets
                        count++;
                    }
                }
            }
        }
    }
    // Return the final count of good triplets
    return count;
};

//! Example 1:
arr = [3, 0, 1, 1, 9, 7], a = 7, b = 2, c = 3
console.log(countGoodTriplets(arr, a, b, c))
// Output: 4
// Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].

//! Example 2:
arr = [1, 1, 2, 2, 3], a = 0, b = 0, c = 1
console.log(countGoodTriplets(arr, a, b, c))
// Output: 0
// Explanation: No triplet satisfies all conditions.
