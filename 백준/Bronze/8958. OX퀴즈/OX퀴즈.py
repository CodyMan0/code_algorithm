n = int(input())

for i in range(n) :
    value = input()
    answer = 0
    plus = 0
    for j in range(len(value)) :
        if value[j-1] =='O' and value[j] == 'O': 
            plus += 1
            answer += plus
        elif value[j] == 'O' :
            plus = 1
            answer += plus
        elif value[j] == 'X' :
            plus = 0
    print(answer)

