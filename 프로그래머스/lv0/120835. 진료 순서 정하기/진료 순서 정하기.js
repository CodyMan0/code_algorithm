function solution(emergency) {
    let n = emergency.length;
    let answer = Array.from({length:n} , () => 1);
    
    for(let i =0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            console.log(emergency[i] ,emergency[j])
            if(emergency[j] > emergency[i]) answer[i]++;
        }
    }
        return answer
}