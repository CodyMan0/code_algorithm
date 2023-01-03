function solution(x, n) {
    let element = 0;
    let result =[];
    for (let i = 0; i < n ; i++ ) {
        element += x
        result.push(element)
    }
    return result;
}