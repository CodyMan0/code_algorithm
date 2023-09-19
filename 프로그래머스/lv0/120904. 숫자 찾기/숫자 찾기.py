def solution(num, k):
    answer = -1
    number = str(num)
    target = str(k)
    
    for i in number : 
        if i == target:
            answer = number.index(i) + 1
        
  
    return answer