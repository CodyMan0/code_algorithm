n = int(input())
data = list(map(int,input().split()))

young = 0
min = 0

for i in data :
    young = young + (((i // 30)+ 1) * 10)
    min = min + (((i // 60)+ 1) * 15)

if young == min :
    print('Y',"M", young)
elif min > young :
    print('Y', young)
else :
    print('M', min)