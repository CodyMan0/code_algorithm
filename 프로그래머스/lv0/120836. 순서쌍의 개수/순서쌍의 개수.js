function solution(n) {
 let result = [];
	for (let i = 1; i <= n; i++) {
		if (Number.isInteger(n / i)) {
			result.push([i, n / i]);
		}
	}
	return result.length;
}