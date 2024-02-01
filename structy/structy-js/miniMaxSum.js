function miniMaxSum(arr) {
	let array = arr.sort();
	let min = 0;
	let max = 0;
	for (let i = 0; i < 4; i++) {
		min += array[i];
	}
	for (let j = 1; j < 5; j++) {
		max += array[j];
	}
	console.log(min,max);
}

let arr = [1, 3, 5, 7, 9];
console.log(miniMaxSum(arr));
