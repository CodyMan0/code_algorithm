function solution(n)
{let answer;
	answer = n
		.toString()
		.split("")
		.reduce((a, b) => Number(a) + Number(b),0);

	return answer;}