n = int(input())
dict = {}
for _ in range(n):
    user = input()
    length = len(user)
    mid = (length//2)
    dict[user] = (length, user[mid])

for i in dict :
    if i[::-1] in dict :
        print(*dict.get(i))
        break
        

