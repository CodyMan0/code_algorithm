function solution (n, lost, reserve) {
    let answer = n-lost.length;
    let checkLost = lost.filter((el) => !reserve.includes(el))
    let checkReserve = reserve.filter((el) => !lost.includes(el))
    
    answer += lost.length - checkLost.length;
    
    
    checkLost.sort((a,b)=>a-b)
    
    checkLost.forEach((el) => {
        if(checkReserve.length === 0){
            return;
        }
        
        if(checkReserve.includes(el-1)){
            console.log('b',checkReserve)
            checkReserve = checkReserve.filter((l) => l !== el -1 )
            console.log('a',checkReserve)
            answer ++;
        }
        else if (checkReserve.includes(el + 1)){
            console.log('b+1',checkReserve)
                 checkReserve = checkReserve.filter((l) => l !== el+1)
            console.log('a',checkReserve)
                answer++;
        }
    })
    

    return answer;
}