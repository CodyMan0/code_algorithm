function solution(order) {
    if(order === 0 ) return 0
    const arr = [...(order+"")]
    let result= 0;
    arr.forEach((el)=>{
        
        if(el % 3 === 0) result++
        if(el === '0') result --
    })
    return result;
}