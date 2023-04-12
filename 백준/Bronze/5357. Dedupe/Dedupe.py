n = int(input())

for i in range(n) :
    prev =''
    value = input()
    for i in range(len(value)):
        if prev != value[i]:
            print(value[i] , end = '')
            prev = value[i]
    print()

