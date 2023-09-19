a, b = map(int,input().split())
c, d = map(int,input().split())

print(b + c if a + d >= b + c else a+d)