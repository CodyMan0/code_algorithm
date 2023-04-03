// 현수의 아빠는 제과점을 운영합니다. 현수 아빠는 현수에게 N일 동안의 매출기록을 주고 연속 된 K일 동안의 최대 매출액이 얼마인지 구하라고 했습니다.
// 만약 N=10이고 10일 간의 매출기록이 아래와 같습니다. 이때 K=3이면
// 12 15 11 20 25 10 20 19 13 15
// 연속된 3일간의 최대 매출액은 11+20+25=56만원입니다. 여러분이 현수를 도와주세요.

//입력 조건 n은 5에서 10만 그리고 숫자열은 각각 500이하의 음이 아닌 정수를 말한다.

//이중포문 안됨 (O(n2))
// 투포인터 알고리즘?
// 배열 자체를 변경할까?
// 슬라이드 알고리즘 O(n)

function solution(k, arr) {
	let answer;
	let sum = 0;

	for (let i = 0; i < k; i++) {
		sum += arr[i];
	}

	answer = sum;

	for (let i = k; i < arr.length; i++) {
		//슬라이딩 알고리즘의 핵심 이것밖에 없었다
		sum += arr[i] - arr[i - k];
		answer = Math.max(answer, sum);
	}

	return answer;
}

let numberList = [12, 15, 11, 20, 25, 10, 20, 19, 13, 15];

console.log(solution(3, numberList));
