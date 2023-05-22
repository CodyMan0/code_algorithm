a, b = map(str, input().split())


max_a= a.replace('5','6')
max_b = b.replace('5','6')


min_a= a.replace('6','5')
min_b = b.replace('6','5')


print(int(min_a) + int(min_b),int(max_a) + int(max_b),sep=' ')
