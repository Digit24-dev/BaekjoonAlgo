import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(start_x, start_y):
    cnt = 1
    q = deque([(start_x, start_y)])
    graph[start_x][start_y] = 0

    while q:
        x, y = q.popleft()
        # cnt += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 1:
                cnt += 1
                graph[nx][ny] = 0
                q.append((nx, ny))
    return cnt
    
result = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            result.append(bfs(i, j))

print(len(result))
for i in sorted(result):
    print(i)