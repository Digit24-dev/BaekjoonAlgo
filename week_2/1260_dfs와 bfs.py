from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)] 
visited = [False] * (N + 1)

# 입력 받기
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(start):
    print(start, end=' ')
    visited[start] = True

    for i in range(1, N+1):
        if visited[i] == False and graph[start][i] != 0:
            dfs(i)

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        cur = q.popleft()
        print(cur, end=' ')
        
        for i in range(1, N+1):
            # print('bfs::::', i, graph[start][i])
            if visited[i] == False and graph[cur][i] != 0:
                visited[i] = True
                q.append(i)

dfs(V)
print()
visited = [False] * (N + 1)
bfs(V)
print()