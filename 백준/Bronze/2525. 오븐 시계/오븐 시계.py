# 시작 시간 소요 시간(천분)
# 분 단위 

hour, min = map(int,input().split())
required_time = int(input())

change_hour = hour * 60
end = change_hour + min + required_time

result_hour = end // 60
result_min = end % 60


if result_hour == 24 : 
    result_hour = 0
elif result_hour > 24 :
    result_hour = 0 + result_hour - 24
    

print(result_hour, result_min)

