n = int(input())
count = 0
for i in list(map(int,input().split())) :
    if n == i :
        count += 1
    else :
        continue
print(count)