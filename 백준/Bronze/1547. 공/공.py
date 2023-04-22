
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

ball = 1
for i in data :
    if i[0] == ball :
        ball = i[1]
        continue
    
    if(i[1] == ball) : ball = i[0]

print(ball)
