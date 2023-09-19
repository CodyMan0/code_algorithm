a = int(input())
b = int(input())
c = int(input())

result = [0] * 10
data = str(a * b * c)

for i in data: 
    result[int(i)] += 1

for i in result :
    print(i)