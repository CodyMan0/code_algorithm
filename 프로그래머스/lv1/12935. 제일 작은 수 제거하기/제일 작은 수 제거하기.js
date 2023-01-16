function solution(arr) {
    const copy = [...arr]
    const min = copy.sort((a,b) => a-b)[0]
    
    const pop = arr.filter((v)=> v !== min)
    console.log(pop)
    


    return copy.length === 1 ? [-1] : pop;
}