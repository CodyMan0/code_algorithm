function solution(money) {
    let num =  Math.floor(money / 5500);
    let leftAccount = money % 5500
    return [
        num,
        leftAccount
    ];
}