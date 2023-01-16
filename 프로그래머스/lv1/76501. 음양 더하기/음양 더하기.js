function solution(absolutes, signs) {
    var answer = 123456789;
    const arr = absolutes.map((v,i)=> {
        if(signs[i]) return v
        else return -v
    })
    const add = arr.reduce((a,b) => a+b)
    return add;
}