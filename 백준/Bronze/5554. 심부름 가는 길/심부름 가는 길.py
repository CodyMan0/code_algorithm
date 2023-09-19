a = int(input())
b = int(input())
c = int(input())
d = int(input())

min = (a + b + c + d) // 60
sec = (a + b + c + d)  % 60
print(min)
print(sec)