function solution(arr){
    const stack=[]
    for(const i of arr){
        
        if(stack[stack.length-1]===i){
            continue
        }
        stack.push(i)
    }
    console.log(stack)
    return stack
}