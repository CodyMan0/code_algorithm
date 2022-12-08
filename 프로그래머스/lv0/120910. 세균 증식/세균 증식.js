function solution(n, t) {
   let answer = [n];
	for (let i = 1; i <= t; i++) {
		answer.push(answer[i - 1] * 2);
	}
    return answer[t];
}