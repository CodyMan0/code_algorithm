P , K = map(int, input().split())
result = K 

for i in range(2,K) :
    if P % i == 0 :
        if result > i :
            result = i

if result != K :
    print('BAD', result)
else :
    print('GOOD')