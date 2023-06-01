# string으로 값에 접근하려면 hash table이 좋을 것 같다. 
# 동명 이인 처리는 어떻게 할까? 

# 입력 
## part는 10만 이하 , com은 part보다 1 작음 즉 반환값이 string 하나 

# 아이디어
## Map (string : number)
## partcipant 배열로 맵 자료구조에 데이터를 저장하고 completion 배열로 맵 자료구조의 데이터를 삭제한다.
## value가 1인 key를 리턴한다.



def solution(participant, completion):
    dict = {}
    for i in participant : 
        if dict.get(i) == None :
            dict[i] = 1
        else :
            dict[i] = dict.get(i) + 1

    for i in completion : 
        dict[i] = dict.get(i) - 1

    for key, value in dict.items() :
        if value == 1 :
            return key