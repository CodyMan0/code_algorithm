function solution(num_list) {
  let answer
  let oddNum = num_list.filter((num)=>num % 2 === 0);
  let evenNum = num_list.filter((num)=>num % 2 == 1);
  answer = [oddNum.length,evenNum.length]
    return answer;
}

function solution2(num_list) {

  return([
 num_list.filter((num)=>num % 2 === 0).length,
 num_list.filter((num)=>num % 2 == 1).length
  ])

}


// 다른 사람

function solution1(num_list) {

  let answer = [0,0];
  for(let a of num_list) {
    answer[a%2] += 1
  }
return (answer)

}
