from collections import deque
# 1번 부터 N번 

# 입력 정점 개수 1부터 1000, 간선 개수 (1부터 1만 ), v (시작) 

n,m,start = map(int,input().split())
graph = [[False] * (n + 1) for _ in range(n+1)]

for _ in range(m) :
    a,b = map(int,input().split())
    graph[a][b] = True
    graph[b][a] = True

visited1 = [False] * (n+1)
visited2 = [False] * (n+1)

def dfs (v) :
    visited1[v] = True
    print(v, end=" ")
    for i in range(1,n+1) :
      if not visited1[i] and graph[v][i]:
        dfs(i)

    
def bfs (start) :
    queue = deque([start])
    visited2[start] = True
    while queue : 
        start = queue.popleft()
        print(start, end=" ")
        for i in range(1,n + 1) :
          if not visited2[i] and graph[start][i]:
            queue.append(i)
            visited2[i] = True
    


dfs(start)
print()
bfs(start)