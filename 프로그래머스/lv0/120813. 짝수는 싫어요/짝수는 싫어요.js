function solution(n) {
  let test = [];
	for (let i = 1; i <= n; i++) {
		if (i % 2 === 1) {
			test = [...test, i];
		}
	}  
    return test
}