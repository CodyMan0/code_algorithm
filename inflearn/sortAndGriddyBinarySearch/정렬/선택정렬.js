// N개이 숫자가 입력되면 오름차순으로 정렬하여 출력하는 프로그램을 작성하세요. 정렬하는 방법은 선택정렬입니다.

function solution(arr) {
	let answer = arr;

	for (let i = 0; i < arr.length - 1; i++) {
		let minValue = i;
		for (let j = i + 1; j < arr.length; j++) {
			if (arr[j] < arr[minValue]) {
				minValue = j;
			}
		}
		console.log(minValue);
		let temp = arr[i];
		arr[i] = arr[minValue];
		arr[minValue] = temp;
	}

	return answer;
}

let arr = [13, 5, 11, 7, 23, 15];
console.log(solution(arr));
