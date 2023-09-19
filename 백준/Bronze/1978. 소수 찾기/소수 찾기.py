# n = int(input())
# arr = list(map(int, input().split()))

# count = 0
# def prime(x) : 
#   for i in range(2, x):
#       if x % i == 0:
#         return False # 소수가 아님
#   return True # 소수임

# for i in arr : 
#    if i == 0 or i == 1 :
#       continue
#    if prime(i) == True :
#       count += 1

# print(count)

# 다른 사람 풀이
input()
l = list(map(int, input().split()))
count = 0

for x in l:
  if x <= 1: continue
  for j in range(2, int(x ** 1/2)+1):
    if x % j == 0: break
  else:
    count += 1

print(count)
