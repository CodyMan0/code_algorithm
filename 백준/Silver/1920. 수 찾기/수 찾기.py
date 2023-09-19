# 입력
# 첫째 줄 자연수 N 
# 둘째 줄 N의 정수
# 셋째 줄 자연수 M
# 넷째 줄 M의 정수 


# N에 M이 있는지 없는지 판단.


n = int(input())
n_arr = list(map(int,input().split()))
n_arr.sort()
m = int(input())
m_arr = list(map(int,input().split()))


def binary_search(arr , target , start, end) :
    if start > end :
        return None
    
    mid = (start + end) // 2
    if arr[mid] == target :
        return mid
    elif arr[mid] > target :
        return binary_search(arr, target, start, mid - 1)
    else :
        return binary_search(arr, target, mid + 1, end)

for i in m_arr :
    result = binary_search(n_arr, i , 0 , n - 1)
    if result == None :
        print(0)
    else :
        print(1)
    