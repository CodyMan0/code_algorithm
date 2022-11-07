function solution(num_list) {
  let answer
  let oddNum = num_list.filter((num)=>num % 2 === 0);
  let evenNum = num_list.filter((num)=>num % 2 == 1);
  answer = [oddNum.length,evenNum.length]
    return answer;
}