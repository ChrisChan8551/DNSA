function plusMinus(arr) {
	let positive = 0;
	let negative = 0;
	let zero = 0;

	for (let i = 0; i < arr.length; i++) {
		console.log(arr[i]);
		if (arr[i] > 0) positive += 1;
		if (arr[i] < 0) negative += 1;
		if (arr[i] === 0) zero += 1;
	}
	console.log((positive / arr.length).toFixed(6));
	console.log((negative / arr.length).toFixed(6));
	console.log((zero / arr.length).toFixed(6));
}

let arr = [1, 2, 3, -1, -2, -3, 0, 0];
plusMinus(arr);
