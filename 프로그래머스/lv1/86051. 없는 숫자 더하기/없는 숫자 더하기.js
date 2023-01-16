function solution(numbers) {
    const result =numbers.reduce((a,b) => a+b)

    return 45-result;
}