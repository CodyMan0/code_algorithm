value = str(input())
result = ""
for i in value:
    if i.islower() :
        result += i.upper()
    else: 
        result += i.lower()

print(result)
