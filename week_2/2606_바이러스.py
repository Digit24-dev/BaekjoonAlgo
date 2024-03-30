import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[0] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

virus = 0

def bfs(i):
    global virus
    q = deque()
    q.append(i)
    visited[i] = True
    
    while q:
        cur = q.popleft()

        for k in range(1, N + 1):
            if visited[k] == False and graph[cur][k] == 1:
                visited[k] = True
                q.append(k)
                virus += 1

bfs(1)

print(virus)