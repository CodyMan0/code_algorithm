queue = int(input())
arr = list(map(int,input().split()))
arr.sort()
result = 0
index = 0 
for i in range(1,queue+1):
    copy_arr = arr[index : i]
    result = result + sum(copy_arr)


print(result)