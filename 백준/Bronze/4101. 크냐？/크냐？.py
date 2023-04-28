while True :
    
    n, m = map(int,input().split())
    if n == 0 : break

    result = 'No' if n <= m else "Yes"
    print(result)

