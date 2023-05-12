# 높이 V 미터
# 낮 A미터 잠 자면서 B미터까지 미끄러짐 V에 가면 안 떨어짐. 

a,b,v = map(int,input().split())
k = (v-b) / (a-b)
print(int(k) if k == int(k) else int(k)+1)