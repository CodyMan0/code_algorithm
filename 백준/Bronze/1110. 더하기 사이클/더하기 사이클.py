n = int(input())

result = 0
pivot = n
prev = n

while True :
    ten = prev // 10
    one = prev % 10
    next_one = (ten + one)%10
    next_ten = one
    next = next_ten*10 + next_one
    prev = next
    result += 1   

    if next == pivot : break

print(result)