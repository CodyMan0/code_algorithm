function solution(x) {
    const string = x.toString()
    const sumX = string.split('').map(el => Number(el)).reduce((acc,cur) => acc + cur,0)
    return x % sumX === 0;
}