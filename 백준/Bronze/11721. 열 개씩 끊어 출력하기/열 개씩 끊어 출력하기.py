n = input()

for i in range(len(n)) :
    if i % 10 == 0 and i != 0 :
        print()
    print(n[i] , end = '')