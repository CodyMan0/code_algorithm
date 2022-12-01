function solution(n) {
    const answer = parseInt(n / 5) + Math.floor((n % 5) / 3) + ((n % 5) % 3);
    return answer;
}