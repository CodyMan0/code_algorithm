function solution(seoul) {
    let index = 0
    seoul.forEach((el,i) => { if(el === 'Kim') index = i})
    return `김서방은 ${index}에 있다`
}