function solution(my_string) {
	const regex = /[^0-9]/g;
	const extract = my_string.replace(regex, "");

	return extract
		.split("")
		.sort((a, b) => a - b)
		.map((i) => Number(i));
}
