n , k = map(int,input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)
account = k
result = 0

for i in coin :
    if k >= i :
        result += account // i
        account = account - (i * (account // i))
    if account == 0 :
        break
    

print(result)


