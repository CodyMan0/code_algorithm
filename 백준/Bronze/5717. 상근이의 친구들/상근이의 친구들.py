result = 0

while True:
    data = list(map(int,input().split()))
    if data[0] == 0 : break 
    result = data[0] + data[1]
    print(result)
