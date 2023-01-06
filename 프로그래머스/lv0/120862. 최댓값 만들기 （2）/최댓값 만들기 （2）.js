const solution = (numbers) => {
    let newArray = [...numbers];
    let result = [];
    for(let i = 0; i < numbers.length; i++) {
        let maxMultipleNum = [];
        newArray.shift(i)
        for(let j = 0; j < newArray.length; j++){
            maxMultipleNum.push(numbers[i] * newArray[j])
            }
        result.push(Math.max(...maxMultipleNum))
        }
    return result.sort((a,b) => b-a)[0]
}