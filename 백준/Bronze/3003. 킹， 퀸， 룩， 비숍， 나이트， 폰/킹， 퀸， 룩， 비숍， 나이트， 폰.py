input = list(map(int, input().split()))
set = [1,1,2,2,2,8]
result = []
for i in range(len(input)):
    print(-(input[i] - set[i]))


