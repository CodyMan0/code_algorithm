
for i in range(3) :
    data = list(map(int, input().split()))

    start = data[:3]
    end = data[3:]
    [h,m,s] = [0]*3
  
    h = end[0] - start[0]
    if end[1] - start[1] < 0 :
        if h < 0 :
            h = 22 - h 
        else :
            h -= 1
        m = 60 - (start[1] - end[1])
    else : 
        m = end[1] - start[1]
        
      
    if end[2] - start[2] < 0 :
        if m == 0 :
            m = 59
            h -= 1
        else :
            m -= 1
        s = 60 - (start[2] - end[2])
    else :
        s = end[2] - start[2]
    
    print(h,m,s ,sep=' ')




    

