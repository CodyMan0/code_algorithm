
# DFS보다는 BFS 풀이가 더 깔끔하다 재귀적 특정 때문에 시간초과가 일어나 모듈을 사용했는데 BFS는 시간초과가 나지 않는다. 코드 수정해보자
# import sys
# sys.setrecursionlimit(10000)


# t = int(input())

# def dfs (x,y):
#     dx = [-1 , 0 , 1, 0]
#     dy = [0 , 1 , 0, -1]

#     for i in range(4):
#         nx = x+ dx[i]
#         ny = y+ dy[i]
#         if ( 0 <= nx < m) and (0 <= ny < n) : 
#             if graph[ny][nx] == 1 : 
#                 graph[ny][nx] = -1
#                 dfs(nx,ny)



# for i in range(t) :
#     m,n,k = map(int,input().split())
#     graph = [[0] * m for _ in range(n)]
#     cnt=0 

#     for j in range(k) :
#         a , b = map(int,input().split())
#         graph[b][a] = 1
#     for x in range(m) :
#         for y in range(n):
#             if graph[y][x] == 1:
#                 dfs(x,y)
#                 cnt += 1
#     print(cnt)
    
    
t =int(input())
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# dfs와 다르게 큐를 통해 너비 우선 탐색을 진행한다. 
def bfs(x,y) :
    queue = [(x,y)]
    graph[x][y] = 0
    while queue :
        x,y = queue.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y+ dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] == 1 :
                queue.append((nx,ny))
                graph[nx][ny] = 0

for _ in range(t) :
    m,n,k= map(int,input().split())
    graph = [[0] * n for _ in range(m)]
    cnt =0
    for _ in range(k) :
        x,y= map(int,input().split())
        graph[x][y] = 1
    
    for a in range(m):
        for  b in range(n) :
            print(a,b)
            if graph[a][b] == 1:
                bfs(a,b)
                cnt += 1
    print(cnt)

# 익숙해질거야!! 조금만 기다려라 그래프 탐색
