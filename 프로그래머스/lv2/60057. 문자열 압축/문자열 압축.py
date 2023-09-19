
    
    
def solution(s):
    answer = len(s)
    
    for step in range(1,len(s) // 2 + 1) : 
        compressed = ''
        prev = s[0 : step]
        count = 1
        ## 단위(count) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step) :
        ## 이전 상태와 동일하다면 압축 횟수 증가 
            if prev == s[j:j +step] :
                count += 1
            else :
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j : j + step]
                count = 1
        
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
        
    return answer