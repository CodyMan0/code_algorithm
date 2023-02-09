function solution(balls, share) {
    console.log(balls,share)
    const factorial = (num) => {
        let arr = Array.from({length: num}, (v, i) => i+1);
        let result = BigInt(1)
        const multiple = arr.map((el) => {
            return result *= BigInt(el)})
        return result
    }
    let answer = factorial(balls) / (factorial(balls-share) * factorial(share))
    
    
    return answer;
}