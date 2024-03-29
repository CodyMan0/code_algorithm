// 임의의 N개의 숫자가 입력으로 주어집니다.
// N개의 수를 오름차순으로 정렬한 다음 N개의 수 중 한 개의 수인 M이 주어지면
// 이분검색으로 M이 정렬된 상태에서 몇 번째에 있는지 구하는 프로그램을 작성하세요.
// 단 중복값은 존재하지 않습니다.

function solution(target, arr) {
	let answer;
	// 들어오는 배열을 오름차순으로 정렬
	arr.sort((a, b) => a - b);
	let leftIndex = 0;
	let rightIndex = arr.length - 1;
	// 큰 조건
	while (leftIndex <= rightIndex) {
		// 미드 변수 선언
		let mid = parseInt((leftIndex + rightIndex) / 2);
		// 세분화된 조건
		if (arr[mid] === target) {
			answer = mid + 1;
			break;
		} else if (arr[mid] > target) {
			rightIndex = mid - 1;
		} else {
			leftIndex = mid + 1;
		}
	}

	return answer;
}

let arr = [23, 87, 65, 12, 57, 32, 99, 81];
console.log(solution(12, arr));
