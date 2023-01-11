function solution(a, b) {
    if(a === b) return a || b;
    
    let answer = 0;
    
    const bigArg = a < b ? b : a    
    const smallArg = a > b ? b : a  
    console.log(bigArg)
    console.log(smallArg)

    let result = [];
    
    for (let i = smallArg ; i <= bigArg; i ++) {
        result.push(i)
    }
    return result.reduce((a,b)=>(a+b),0);
}