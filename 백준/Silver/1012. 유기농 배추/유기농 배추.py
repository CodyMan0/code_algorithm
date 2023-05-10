
import sys
sys.setrecursionlimit(10000)


t = int(input())

def dfs (x,y):
    dx = [-1 , 0 , 1, 0]
    dy = [0 , 1 , 0, -1]

    for i in range(4):
        nx = x+ dx[i]
        ny = y+ dy[i]
        if ( 0 <= nx < m) and (0 <= ny < n) : 
            if graph[ny][nx] == 1 : 
                graph[ny][nx] = -1
                dfs(nx,ny)



for i in range(t) :
    m,n,k = map(int,input().split())
    graph = [[0] * m for _ in range(n)]
    cnt=0 

    for j in range(k) :
        a , b = map(int,input().split())
        graph[b][a] = 1
    for x in range(m) :
        for y in range(n):
            if graph[y][x] == 1:
                dfs(x,y)
                cnt += 1
    print(cnt)
    
