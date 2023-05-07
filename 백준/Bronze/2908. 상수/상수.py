a, b = map(str, input().split())
aa = a[::-1]
bb = b[::-1]

print(int(aa) if int(aa) > int(bb) else int(bb))
