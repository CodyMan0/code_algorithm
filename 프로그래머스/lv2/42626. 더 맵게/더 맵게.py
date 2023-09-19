# 처음 입력 들어올때 정렬하고 
# 섞고 나서 정렬해야한다.  
## 이부분을 자료구조로 대체!! 힙을 활용해서 정렬되도록 한다.


# 출력 

# 모든 요소가 K보다 크다는 것을 어떻게 판단하지? 

# 조건
## scoville 2부터 100만
## K는 0이상 10억 이하 
## K이상으로 만들 수 없을때 -1 return


import heapq

def solution(scoville, K):    
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K :
        if len(scoville) > 1 :
            answer += 1
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            heapq.heappush(scoville, first + second * 2)
        else :
            return -1
    return answer