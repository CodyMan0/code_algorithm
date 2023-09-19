data = [input() for _ in range(5)]

result = []
for i in data :
    if i.find("FBI") >= 0 :
        result.append(data.index(i) + 1)
    
if len(result) == 0 :
    print("HE GOT AWAY!")
else :
    print(' '.join(str(s) for s in result))



