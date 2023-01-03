function solution(array) {
    let comparedTarget = [0,0];
    for (let i = 0; i < array.length; i++) {
        console.log(comparedTarget)
        if(comparedTarget[0] < array[i]) comparedTarget = [array[i],i]
    }
    return comparedTarget;
}