

// https://leetcode.com/problems/can-place-flowers
// You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

// Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.



//! Example 1:
// Input: flowerbed = [1,0,0,0,1], n = 1
// Output: true

//! Example 2:
// Input: flowerbed = [1,0,0,0,1], n = 2
// Output: false


// Constraints:

// 1 <= flowerbed.length <= 2 * 104
// flowerbed[i] is 0 or 1.
// There are no two adjacent flowers in flowerbed.
// 0 <= n <= flowerbed.length

const canPlaceFlowers = (flowerbed, n) => {
    let count = 0;
    let i = 0;

    while (i < flowerbed.length) {
        if (flowerbed[i] === 0) {
            // Check if the current position and its neighbors are empty
            if ((i === 0 || flowerbed[i - 1] === 0) && (i === flowerbed.length - 1 || flowerbed[i + 1] === 0)) {
                flowerbed[i] = 1;  // Plant a flower
                count += 1;
            }
        }
        i += 1;
    }

    return count >= n;

}

//! Example 1:
flowerbed = [1, 0, 0, 0, 1]
n = 1
console.log(canPlaceFlowers(flowerbed, n))
// Output: true

//! Example 2:
flowerbed = [1, 0, 0, 0, 1]
n = 2
console.log(canPlaceFlowers(flowerbed, n))
// Output: false
