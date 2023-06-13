# 전체 학생 수 2명 30명 
# lost와 reserve에 동일한 번호가 있을 경우 처리햐야한다. 

## 조건 
## 자신보다 1 작거나 클 경우에만 빌려줄 수 있다. 
## 그게 아니면 n -= -1 
## n이 0이면 리턴 



def solution(n, lost, reserve):
    set_reserve = set(reserve)-set(lost)
    set_lost = set(lost) - set(reserve)
    for i in set_reserve :
        if i - 1 in set_lost :
            set_lost.remove(i - 1)
        elif i + 1 in set_lost :
            set_lost.remove(i+1)
    return n - len(set_lost)

        
    return answer