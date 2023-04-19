from sys import stdin

for _ in range(3):
    N = int(stdin.readline())
    list = [int(stdin.readline()) for i in range(N)]
    if sum(list) == 0:
        print("0")
    elif sum(list) > 0:
        print("+")
    else:
        print("-")