# 점수 중 최댓값 m  모든 점수를 점수 / m * 100

n = int(input())
score= list(map(int, input().split()))
max_score = max(score)
new_list = []

for s in score : 
    new_list.append(s/max_score * 100)

test_avg = sum(new_list) / n

print(test_avg)