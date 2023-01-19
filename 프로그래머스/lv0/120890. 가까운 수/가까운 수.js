function solution(array, n) {
    let result = 0;
    var answer = Number.MAX_SAFE_INTEGER;
    array.sort((a,b) => a-b)
    for (let i = 0 ; i < array.length; i++) {
        if (answer > Math.abs(n-array[i])) {
            answer = Math.abs(n-array[i])
            result = array[i]
        }
    }

    console.log(result)
    return result;
}