function solution([...rsp]) {
    let arr = {
        2: 0,
        0: 5,
        5: 2
    };
    var answer = rsp.map(v => arr[v]).join("");
    return answer;
}