
while True :
    name,age,weight=input().split()
    age=int(age)
    weight=int(weight)
    if '#' in name:
        quit()
    if int(age) > 17 or int(weight) >= 80 :
        print(f"{name} Senior")
    else : 
        print(f"{name} Junior")

