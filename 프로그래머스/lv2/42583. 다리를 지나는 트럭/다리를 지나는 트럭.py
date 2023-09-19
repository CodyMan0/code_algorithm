

def solution(l, w, n):
    answer = 0
    sum_bridge = 0
    bridge = [0 for _ in range(l)]
    
    while bridge :
        answer += 1 
        sum_bridge -= bridge[0]
        bridge.pop(0)
        
        if n : 
            if sum_bridge + n[0] <= w :
                sum_bridge += n[0]
                t = n.pop(0)
                bridge.append(t)
            else :
                bridge.append(0)
    return answer
            
        
        
