function solution(numbers) {
    const sum = numbers.reduce((a,b) => (a+b));
    let result = sum/numbers.length 
    return result;
}