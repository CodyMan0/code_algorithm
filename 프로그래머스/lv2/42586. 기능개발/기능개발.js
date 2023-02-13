function solution(progresses, speeds) {
    let answer= [0]
    //우선 몇일이 걸리는지를 파악하는 로직을 작성
    const depDay= progresses.map((el,i) => {
        const day = Math.ceil(((100-el )/ speeds[i]))
        return day;
    })
    
    let maxDay = depDay[0];

    
    for ( let i =0, j = 0 ; i< depDay.length; i++) {
        if(depDay[i] <= maxDay) {
        answer[j] += 1
        } else {
            maxDay = depDay[i]
            answer[++j] = 1;
        }
        
    }
    
    

    
    return answer;
}