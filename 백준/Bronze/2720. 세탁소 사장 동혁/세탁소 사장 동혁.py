n = int(input())

for i in range(n) :
    change = int(input())
    quarter = change // 25
    dime = (change%25) // 10
    nikel = (change%25%10) // 5
    penny = (change%25%10%5) // 1
    print(quarter, dime, nikel, penny)