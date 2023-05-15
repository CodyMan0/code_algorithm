
n = int(input())
s = input()


single = s.count("S")
couple = s.count("L")

holder = 1 + single + (couple // 2)

if single + couple > holder :
    print(holder)
else :
    print(single + couple)