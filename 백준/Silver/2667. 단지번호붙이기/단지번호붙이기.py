
import sys
from collections import deque

# dx = [-1,0,1,0]
# dy =[0,1,0,-1]


# def bfs (x,y) : 
#     print('---------------',x,y)
#     q = deque()
#     q.append((x,y))
#     count = 0
    
#     while q :
#         x,y = q.popleft()
#         for i in range(4) :
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < n :
#                 if graph[nx][ny] != 0:
#                     graph[nx][ny]= True
#                     count += 1
#     return count
        
            


# n = int(input())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int,input())))

# print(graph)

# result = 0 
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == False :
#             bfs(i,j)
#             result += 1

# print(result)

# 핵심 탐색 중 1인 부분은 0으로 바꿔서 다시 방문치 않도록

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(graph, x, y) :
    n = len(graph)
    q = deque()
    q.append((x,y))
    graph[x][y] = 0
    cnt = 1
    while q : 
        xx , yy = q.popleft()
        for i in range(4) :
            nx = xx + dx[i]
            ny = yy + dy[i]
            if 0 <= nx < n and 0 <= ny < n :
                if graph[nx][ny] == 1 :
                    graph[nx][ny] = 0 
                    q.append((nx,ny))
                    cnt += 1
    return cnt 
                

n = int(input())
graph = []
for i in range(n) : 
    graph.append(list(map(int,input())))

count = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            count.append(bfs(graph,i,j))

count.sort()

print(len(count))
for i in range(len(count)):
    print(count[i])
