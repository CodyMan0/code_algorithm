# 기본적으로 한칸에 1초 
# 앞에 2칸은 비어있다 그래서 1까지 돌아오는데 2초 2는 3초 
n = input()
convert_to_num = [["A","B","C"],['D',"E","F"],["G",'H','I'],["J",'K',"L"],["M","N","O"],["P","Q",'R',"S"],["T","U","V"],["W","X","Y","Z"]]

# 알파벳 문자열에 해당하는 번호 리턴 
num = ''
for i in n :
    cnt = 1
    for j in convert_to_num :
        cnt += 1
        if i in j :
            break
    num += str(cnt)


# 번호에 따른 최소 시간을 구하는 함수 
result = 0
for i in num : 
    start = 1
    result += int(i)+start

print(result)
        
