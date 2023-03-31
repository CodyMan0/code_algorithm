function solution(n, k, cards) {
	let answer;
	let modifiedArr = cards.map((card) => [
		card,
		String(card)
			.split("")
			.reduce((acc, cur) => acc + cur * 1, 0),
	]);
	let max = Number.MIN_SAFE_INTEGER;

	for (let i = 1; i < modifiedArr.length; i++) {
		if (modifiedArr[i][1] > max) {
			max = modifiedArr[i][1];
			answer = modifiedArr[i][0];
		} else {
			continue;
		}
	}
	return answer;
}

let arr = [13, 15, 34, 23, 45, 65, 33, 11, 26, 42];
console.log(solution(10, 3, arr));
