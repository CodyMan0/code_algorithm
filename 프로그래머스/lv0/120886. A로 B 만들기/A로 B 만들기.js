function solution(before, after) {
    const a = before.split("").sort().join("");
    const b = after.split("").sort().join("");
    
    
    return a === b ? 1 : 0;
}