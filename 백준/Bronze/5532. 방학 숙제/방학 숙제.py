import math

l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

max_lang = math.ceil(a / c)
max_math = math.ceil(b / d)
max = 0;

if max_lang >= max_math :
    max = max_lang
else :
    max = max_math
    
print(l - max)
