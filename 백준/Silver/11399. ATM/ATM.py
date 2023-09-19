queue = int(input())
arr = list(map(int,input().split()))
arr.sort()
result = 0
index = 0 
for i in range(1,queue+1):
    copy_arr = arr[index : i]
    result = result + sum(copy_arr)


print(result)

# 얕은 복사를 통해 문제를 풀 수도 있지만, 규칙을 찾아서 풀 수도 있다.

import sys
n = int(sys.stdin.readline())
time = list(map(int, sys.stdin.readline().split()))
time.sort()
sum = 0
for i in range(n) :
    sum += time.pop() * (i + 1)

print(sum)
    
