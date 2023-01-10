function solution(my_string) {
    const result = Array.from(new Set(my_string));
    return result.join("");
}