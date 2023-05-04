value = input()

arr = [-1] * 26

for i in range(len(value)) :
    if arr[ord(value[i])-97] != -1 :
        continue
    arr[ord(value[i])-97] = i


for i in range(len(arr)) : 
  print(arr[i], end=" ")
