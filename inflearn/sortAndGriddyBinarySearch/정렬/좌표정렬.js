function solution(arr) {
	let answer = arr;
	// 이중 배열의 각각 인덱스를 기준으로 해도 배열에는 정렬이 안되는 경우가 있다.

	// 같은 0번 인덱스끼리 배열에 담아야하나?
	// 조건을 통해서 바꿔주면 되나? 바꿔보자
	answer.sort((a, b) => {
		if (a[0] === b[0]) return a[1] - b[1];
		else return a[0] - b[0];
	});
	return answer;
}

let arr = [
	[2, 7],
	[1, 3],
	[1, 2],
	[2, 5],
	[3, 6],
];
console.log(solution(arr));
