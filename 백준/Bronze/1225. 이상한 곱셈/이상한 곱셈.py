import sys
A,B = map(list,sys.stdin.readline().split())
A = list(map(int,A))
B = list(map(int,B))
print(sum(A) * sum(B))


# 유연한 사고를 하자 문제에서 조합을 예로 들어 경우의 수를 생각해야할 것 처럼 유도했지만 곱셈의 원리상
# 일의 자리수부터 해당 자리수까지 다 곱하고 각 자리수를 더해서 최종 값을 만들었잖아. 초등학생때 배운거잖아~ 
# 아주 단순한 문제였는데 낚여버렸다. 
