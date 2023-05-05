n = int(input())
arr = list(map(int, input().split()))

sum = 0
count = 0


for i in range(n) : 
    if arr[i] == 1 :
        count = count + 1
    else :
        count =0
    sum += count

print(sum)
