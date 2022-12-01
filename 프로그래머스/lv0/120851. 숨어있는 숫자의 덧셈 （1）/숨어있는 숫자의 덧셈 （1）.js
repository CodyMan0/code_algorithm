function solution(my_string) {
  let str = my_string.replace(/[^0-9]/g, "");
  const toNumbers = (arr) => arr.map(Number);

  return toNumbers(str.split("")).reduce((a, b) => a + b);
}