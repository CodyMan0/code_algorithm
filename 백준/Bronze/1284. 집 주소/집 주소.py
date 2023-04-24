while True :
    value = int(input())
    if value == 0 :
        break
    to_string_value = str(value)
    first = (len(to_string_value) -1)
    second = 0 
    for i in to_string_value:
        i = int(i)
        if i == 1 :
            second += 2
        elif i == 0 :
            second += 4
        else :
            second += 3

    
    print(first + second + 2)