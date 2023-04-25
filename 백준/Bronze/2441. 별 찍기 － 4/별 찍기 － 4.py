n  =  int(input())

for i in range(1,n+1) :
    a= '*'*(n-(i-1))
    print(f'{a:>{n}}')
