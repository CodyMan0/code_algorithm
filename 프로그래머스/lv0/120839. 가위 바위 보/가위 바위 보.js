function solution(rsp) {
    const result = rsp.split('').map((element) => (
        element === '2' ? '0' : element === '5' ? '2' : '5'))
    
    return result.join('');
}