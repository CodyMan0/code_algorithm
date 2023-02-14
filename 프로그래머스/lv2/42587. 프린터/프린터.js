function solution(priorities, location) {
    let stack = [];
    let waitList = priorities.map((x, i) => [x, i]);
    
    while (waitList.length) {
        const front = waitList.shift();
        console.log(front[1])
        if (front[0] >= Math.max(...waitList.map(x => x[0]))) {
            stack.push(front[1]);
            if (front[1] === location)
                break;
        } else {
            waitList.push(front);
        }
    }
    console.log(stack)
    return stack.indexOf(location) + 1;
}