function solution(answers) {
    const studentOne = [1,2,3,4,5];
    const studentOneLength = studentOne.length;
    
    const studentTwo = [2,1,2,3,2,4,2,5];
    const studentTwoLength = studentTwo.length;
    
    const studentThree = [3,3,1,1,2,2,4,4,5,5];
    const studentThreeLength = studentThree.length;
    
    let correctPoint = [0,0,0];
    let answer = [];
    
    
    for (let i = 0 ; i < answers.length; i ++) {
    if (answers[i] === studentOne[i % studentOneLength]) correctPoint[0]++;
    if (answers[i] === studentTwo[i % studentTwoLength]) correctPoint[1]++;
    if (answers[i] === studentThree[i % studentThreeLength]) correctPoint[2]++;
    }

    const maxResult = Math.max(...correctPoint);
    for(let i = 1; i<= 3; i++) {
        if(maxResult === correctPoint[i-1]) answer.push(i)
    }

    return answer;
}