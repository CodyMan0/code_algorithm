function solution(s) {
    var answer = '';
    const partObj = s.split("").reduce((prev,curr) => {
     if(curr in prev){
            prev[curr]++
        }else{
            prev[curr]=1
        }
    return prev
    },{})
    
    for(const [key,value] of Object.entries(partObj)){
        if(value === 1){
            answer += key
        }
    }
    
    const result =answer.split("").map((el) => {
        return el.charCodeAt() })
    
    const total = result.sort((a,b) => a-b).map((el) => {
        return String.fromCharCode(el)
    }).join("")
    

    return total;
}