function solution(phone_number) {
    console.log(phone_number.slice(-4))
    var answer = '';
    for(let i = 0; i < phone_number.length-4 ; i ++) {
        answer += '*'
    }

    return answer.concat(phone_number.slice(-4));
}