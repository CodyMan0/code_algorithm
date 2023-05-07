# 2000만번 계산 가능 

# s를 받아 각 문자를 R번 반복해 새문자열 P를 만들라
t = int(input())


for i in range(t) : 
    p =''
    r,s = map(str,input().split())
    for j in range(len(s)) :
      p += s[j] * int(r)
    print(p)
    