function solution(arr) {
	let answer = arr;
	for (let i = 1; i < arr.length; i++) {
		let insertingData = arr[i];
		let j;
		for (j = i - 1; j >= 0; j--) {
			if (arr[j] > insertingData) arr[j + 1] = arr[j];
			else break;
		}

		arr[j + 1] = insertingData;
	}
}

let arr = [11, 7, 5, 6, 10, 9];

solution(arr);

console.log(arr);
