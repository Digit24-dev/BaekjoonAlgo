import sys
from collections import deque

m, n, h = map(int, input().split())

matrix = [
    [list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)
]
visited = [[[False] * m for _ in range(n)] for _ in range(h)]

queue = deque()

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

answer = 0


def bfs():
    while queue:
        z, x, y = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nz < 0 or nz >= h or nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if matrix[nz][nx][ny] == 0 and visited[nz][nx][ny] == False:
                queue.append((nz, nx, ny))
                ################################################################
                matrix[nz][nx][ny] = matrix[z][x][y] + 1
                ################################################################
                visited[nz][nx][ny] = True


# 모두 1이 아닐 경우

for i in range(h):
    for j in range(n):
        for k in range(m):
            if matrix[i][j][k] == 1 and visited[i][j][k] == 0:
                queue.append((i, j, k))
                visited[i][j][k] = True
bfs()

# 토마토 확인
for i in matrix:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        answer = max(answer, max(j))

print(answer - 1)

