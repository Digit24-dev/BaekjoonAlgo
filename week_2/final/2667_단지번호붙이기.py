import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

board = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

total = 0

def bfs(i, j):
    houses = 0
    q = deque()
    q.append((i,j))
    visited[i][j] = True

    while q:
        ci, cj = q.popleft()
        houses += 1

        for dir in range(4):
            ni = ci + di[dir]
            nj = cj + dj[dir]

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == False and board[ni][nj] == 1:
                    visited[ni][nj]= True
                    q.append((ni, nj))

    return houses

res = []
for i in range(N):
    for j in range(N):
        # 탐색
        if board[i][j] == 1 and visited[i][j] == False:
            total += 1
            res.append(bfs(i,j))

print(total)
res.sort()

for i in res:
    print(i)