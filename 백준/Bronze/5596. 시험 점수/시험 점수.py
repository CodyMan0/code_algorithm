min = list(map(int,input().split()))
man = list(map(int,input().split()))

if sum(min) == sum(man) :
    print(sum(min))
else :
    print(max(sum(min), sum(man)))
