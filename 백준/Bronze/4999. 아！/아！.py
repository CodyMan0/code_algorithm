n = input()
m = input()

a=0
b=0

for i in range(len(n)) :
    if n[i] =='a' : a +=1 

for i in range(len(m)) :
    if m[i] =='a' : b +=1 


if (a < b) :
    print('no')
else :
    print('go')
    