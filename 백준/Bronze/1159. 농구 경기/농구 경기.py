t = int(input())

list = [0] * 26


for i in range(t) :
    name = input()
    last_name = name[0]
    list[ord(last_name)-97] += 1


if max(list) < 5 :
    print('PREDAJA')
else : 
    result = ''
    for i in range(len(list)) :
        if list[i] > 4 : 
            result += chr(i + 97)
    print(result)








