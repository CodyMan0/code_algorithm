roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def romanToInt(s):
    answer = 0
    print(answer)
    for i in range(len(s) - 1, -1, -1):
        num = roman[s[i]]
        if 4 * num < answer:
            answer -= num
        else:
            answer += num
    return answer


romanToInt("III")
romanToInt("LVIII")
romanToInt("MCMXCIV")
