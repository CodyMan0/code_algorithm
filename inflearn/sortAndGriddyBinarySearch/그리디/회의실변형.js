// 내풀이 방식

// function solution(meeting) {
// 	let answer = [];
// 	for (let i = 0; i < meeting.length; i++) {
// 		let element = meeting[i][1];
// 		let num = 1;
// 		for (let j = 0; j < meeting.length; j++) {
// 			if (meeting[j][0] === element) {
// 				element = meeting[j][1];
// 				num++;
// 			}
// 		}
// 		answer.push(num);
// 	}

// 	return Math.max(...answer);
// }

// let arr = [
// 	[1, 4],
// 	[2, 3],
// 	[3, 5],
// 	[4, 6],
// 	[5, 7],
// ];
// console.log(solution(arr));

// 강의

function solution(meeting) {
	let answer = 0;
	meeting.sort((a, b) => {
		if (a[1] === b[1]) return a[0] - b[0];
		a[1] - b[1];
	});

	let endTime = 0;
	for (let x of meeting) {
		if (x[0] >= endTime) {
			answer++;
			endTime = x[1];
		}
	}

	console.log(meeting);
	return answer;
}

let arr = [
	[3, 3],
	[2, 3],
	[1, 3],
];
console.log(solution(arr));
