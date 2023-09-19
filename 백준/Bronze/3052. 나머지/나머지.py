import sys
data = [int(sys.stdin.readline().strip()) for i in range(10)]

result = []

for i in data :
  if (i % 42) not in result :
    result.append(i % 42)

print(len(result))