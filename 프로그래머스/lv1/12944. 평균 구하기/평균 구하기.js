function solution(arr) {
    let answer;
    let sum = arr.reduce((a,b) => a+b)
    answer = sum / arr.length
    return answer;
}