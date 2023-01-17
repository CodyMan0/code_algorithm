function solution(array, commands) {
    const answer = [];
    const r = commands.map((el)=>{
        const takeElement = array.slice(el[0]-1,el[1]).sort((a,b)=> a-b);
        const result = takeElement[el[2]-1]
        return answer.push(result)
            
    })
    return answer;
}