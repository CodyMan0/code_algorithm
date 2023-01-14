function solution(my_string) {
    const lowercaseArray = [...my_string.toLowerCase()]


    return lowercaseArray.sort().join("");
}