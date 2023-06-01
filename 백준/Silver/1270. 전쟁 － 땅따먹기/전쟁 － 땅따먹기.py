
for _ in range(int(input())) : 
    arr = list(map(int,input().split()))
    reverse_arr = arr[::-1]
    condition_length = reverse_arr.pop() // 2


    dict = {}
    for i in reverse_arr :
        if dict.get(i) == None:
          dict[i] = 1
        else :
          dict[i] = dict.get(i) + 1
    
    answer = 0
    for key,value in dict.items() :
      if value > condition_length :
          answer = key
          print(answer)
          break
    
    if answer == 0 :
      print("SYJKGW") 

