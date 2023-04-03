function solution(s) {
	let answer;
	let hashMap = new Map();

	for (const res of s) {
		if (hashMap.has(res)) {
			hashMap.set(res, hashMap.get(res) + 1);
		} else hashMap.set(res, 1);
	}

	let max = Number.MIN_SAFE_INTEGER;
	for (const [key, value] of hashMap) {
		if (value > max) {
			max = value;
			answer = key;
		}
	}

	return answer;
}

let str = "BACBACCACCBDEDE";
console.log(solution(str));
