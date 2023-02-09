function solution(citations) {
    const copy = [...citations]
    copy.sort((a,b) => b-a)

    let i = 0;
    while (i + 1 <= copy[i]) {
        i++;
    }    
    return i;
}