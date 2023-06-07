def solution(priorities, location):
    answer = 0
    wait_list = [(i,value) for i , value in enumerate(priorities)]
    
    while wait_list : 
        first = wait_list.pop(0)
        if any(first[1] < q[1] for q in wait_list) :
            print('first',first)
            wait_list.append(first)
        else :
            print('else',first)
            answer += 1
            if first[0] == location :
                print(answer)
                return answer

    