
arr = []
max = 0
index = 0

for i in range(1,10) :
    arr.append(int(input()))

for i in range(1,len(arr) + 1) :
    if arr[i-1] > max : 
        max = arr[i-1]
        index = i

print(max)
print(index)

