function solution(age) {
    const arr="abcdefghij"
    
    return [...age.toString()].map(i=>arr[i]).join("")
}