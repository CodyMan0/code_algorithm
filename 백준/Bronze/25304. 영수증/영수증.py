

t = int(input())
n = int(input())
arr = [[] for _ in range(n)]
result = 0
for i in range(n):
    x , y = map(int,input().split())
    arr[i].append(x)
    arr[i].append(y)

for i in range(n) :
    result += arr[i][0] * arr[i][1]

if result == t :
    print("Yes")
else :
    print("No")