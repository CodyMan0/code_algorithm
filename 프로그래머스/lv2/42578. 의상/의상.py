## 조합 같은 경우 라이브러리를 사용해도 될까? 
## 이중 리스트 카테고리로의 접근이 O(n) Map 자료구조로 O(1)

## 이중 배열의 데이터를 맵에 넣어보자 체크

## 조합을 구해보자 

from itertools import combinations

def solution(clothes):
    clothes_map = {}
    for cloth in clothes :
        clothes_map[cloth[1]] = clothes_map.get(cloth[1],0) + 1

    answer = 1
    for type in clothes_map :
        print('b',answer)
        answer *= (clothes_map[type] + 1)
        print('a',answer)
    return answer -1
