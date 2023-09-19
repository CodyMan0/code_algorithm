t = int(input())
for _ in range(t) :
    list_with_range = list(map(int,input().split()))
    arr = list_with_range[1:]
    num = list_with_range[:1][0]
    more_aver_num = 0
    average = sum(arr) / num
    for i in arr :
        if i > average :
            more_aver_num += 1
    print(f'{more_aver_num / num * 100 :.3f}%')
