n , k = map(int,input().split())
coin = [int(input()) for _ in range(n)]
coin.sort(reverse=True)
result = 0

for i in coin :
    if k >= i :
        result += k // i
        k %= i
    if k == 0 :
        break
    

print(result)
