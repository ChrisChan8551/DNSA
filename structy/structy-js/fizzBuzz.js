function fizzBuzz(n) {
	for (let i = 1; i <= n; i++) {
		if (i % 3 === 0 && i % 5 != 0) {
			console.log('Fizz');
		} else if (i % 3 != 0 && i % 5 === 0) {
			console.log('Buzz');
		} else if (i % 3 === 0 && i % 5 === 0) {
			console.log('FizzBuzz');
		} else if (i % 3 !== 0 && i % 5 !== 0) {
			console.log(i);
		} else console.log('NONE');
	}
}

console.log(fizzBuzz(15));
