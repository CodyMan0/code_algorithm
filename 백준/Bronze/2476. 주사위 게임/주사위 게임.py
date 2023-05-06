t = int(input())
result = []
for i in range(t) : 
    arr = list(map(int,input().split()))
    same = 0
    index = 0
    for j in range(len(arr)) : 
        if arr.count(arr[j]) > same : 
            same = arr.count(arr[j])
            index = j
    if same == 3 :
        result.append(10000 + (arr[0] * 1000))
    elif same == 2 :
        result.append(1000 + (arr[index] * 100))
    else :
        result.append(max(arr)* 100)

print(max(result))
    