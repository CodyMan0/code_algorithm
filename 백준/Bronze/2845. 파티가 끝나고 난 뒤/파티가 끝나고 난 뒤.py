number,width = map(int , input().split())
expectedNumber = number * width

data = list(map(int,input().split()))

for i in data :
    print(i - expectedNumber)




