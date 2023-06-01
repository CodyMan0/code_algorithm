
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


# Map을 사용하지 않고 배열 안에서 가장 수가 많은 요소를 찾는 함수를 만들고 외부에서 해당 함수의 리턴값을 count 매소드를 활용하여 위와 동일한 로직을 구현할 수 있다. 

## 어떤게 더 나은 로직일까? 
### 둘다 시간 복잡도는 O(n)인 것 같다. 

import sys

input = sys.stdin.readline

def find_majority_element(lst):
    m = -1
    i = 0
    for j in range(len(lst)):
        if i == 0:
            m = lst[j]
            i = 1
        elif m == lst[j]:
            i += 1
        else:
            i -= 1
    return m


T = int(input())
for _ in range(T):
    lst = list(map(int, input().split()))[1:]
    v = find_majority_element(lst)
    if lst.count(v) > len(lst) // 2:
        print(v)
    else:
        print("SYJKGW")
    
