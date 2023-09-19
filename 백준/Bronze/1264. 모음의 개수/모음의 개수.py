
while True :
    word = input()
    count = 0 
    vowel = ['a','e','i','o','u']
    if word == "#":
        break
    for i in word :
        if i.lower() in vowel: 
            count += 1
    print(count)

