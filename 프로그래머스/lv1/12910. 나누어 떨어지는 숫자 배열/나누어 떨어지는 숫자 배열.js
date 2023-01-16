function solution(arr, divisor) {
    const dividedElement = arr.filter((v,i)=>{
        return v % divisor === 0
    })
   return dividedElement.length === 0 ? [-1] : dividedElement.sort((a,b) => a-b)
}