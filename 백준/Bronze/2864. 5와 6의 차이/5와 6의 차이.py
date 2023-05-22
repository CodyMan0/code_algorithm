a, b = input().split()


max = int(a.replace('5','6')) +int(b.replace('5','6'))
min = int(a.replace('6','5')) + int(b.replace('6','5'))


print(min, max,sep=' ')
