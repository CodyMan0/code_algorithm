n = int(input())
arr = []
for _ in range(n):
    name,a,b,c = map(str, input().split())
    arr.append([name,int(a),int(b),int(c)])


result = sorted(arr, key = lambda x : [-x[1], x[2], -x[3],x[0]] )


for i in range(n):
    print(result[i][0])
