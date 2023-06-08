def solution(priorities, location):
    answer = 0
    wait_list = [(i,value) for i,value in enumerate(priorities)]
    
    while wait_list :
        first = wait_list.pop(0)
        
        if any(first[1] < a[1] for a in wait_list ) :
            wait_list.append(first)
        else :
            answer += 1
            if first[0] == location :
                return answer
   