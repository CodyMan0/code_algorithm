## 내풀이
value = input()

arr = [-1] * 26

for i in range(len(value)) :
    if arr[ord(value[i])-97] != -1 :
        continue
    arr[ord(value[i])-97] = i


for i in range(len(arr)) : 
  print(arr[i], end=" ")

## 다른 사람 풀이

s = input()
for i in range(97,123):
    print(s.find(chr(i)), end=' ')
