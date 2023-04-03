// 쉽게 풀 수 있었지만 배열의 길이가 3만개라면 이건 말도 안된다. 시간 복잡도 O(n2)이면 최대 3만게 일때 너무 성능이 안좋다.
//

function solution(arr1, arr2) {
	let answer = [];

	for (let i = 0; i < arr1.length; i++) {
		for (let j = 0; j < arr2.length; j++) {
			if (arr1[i] === arr2[j]) {
				answer.push(arr1[i]);
			}
		}
	}
`
	return answer.sort((a, b) => a - b);
}

let a = [1, 3, 9, 5, 2];
let b = [3, 2, 5, 7, 8];
console.log(solution(a, b));

// 이중 포문보다 성능이 좋다. O(n)
function solution1(arr1, arr2) {
	let answer = [];
	// 인자 두 배열을 정렬
	arr1.sort((a, b) => a - b);
	arr2.sort((a, b) => a - b);

	// 각각의 포인터 변수 선언
	let firstPointer = 0;
	let secondPointer = 0;
	//while문
	while (firstPointer < arr1.length && secondPointer < arr2.length) {
		if (arr1[firstPointer] === arr2[secondPointer]) {
			// p1과 p2 같을때 푸쉬 후 동시에 증가
			answer.push(arr1[firstPointer++]);
			secondPointer++;
		} else if (arr1[firstPointer] < arr2[secondPointer]) {
			firstPointer++;
		} else {
			secondPointer++;
		}
	}

	return answer;
}

let aa = [1, 3, 9, 5, 2];
let bb = [3, 2, 5, 7, 8];
console.log(solution1(aa, bb));
