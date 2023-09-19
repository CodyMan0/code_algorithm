## 연산  + - * // 네개 
## 음수를 양수로 나눌떄 C++ 14 기준 음수를 양수로 바꾸고 몫을 취하고 그 몫을 음수로 바꿈
## N개의 수와 n-1개의 연산 만들 수 있는 식의 결과 최대와 최소 

n = int(input())

arr = list(map(int,input().split()))



a,s,m,d = map(int,input().split())

min_value= 1e9
max_value = -1e9

def dfs(i,now) :
    global min_value,max_value,a,s,m,d
    if i == n :
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else :
        if a > 0 :
            a -= 1
            dfs(i + 1, now + arr[i])
            a += 1
        if s > 0 :
            s -= 1
            dfs(i + 1, now - arr[i])
            s += 1
        if m > 0 :
            m -= 1
            dfs(i + 1, now * arr[i])
            m += 1
        if d > 0 :
            d -= 1
            dfs(i + 1, int(now / arr[i]))
            d += 1

dfs(1,arr[0])

print(max_value)
print(min_value)



