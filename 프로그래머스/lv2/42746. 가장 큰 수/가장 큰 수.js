function solution(numbers) {
    const _numbers = [...numbers];
    
    const result = _numbers.sort((a, b) => {
        return ('' + b + a) - ('' + a + b);
    }).join('');
   
    return result[0] === '0' ? '0' : result;
}