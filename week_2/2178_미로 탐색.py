import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
mmap = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def debug():
    for i in range(N):
        for j in range(M):
            print(mmap[i][j], end=' ')
        print()

for i in range(N):
    line = input()
    for j in range(M):
        mmap[i][j] = int(line[j])

def bfs(i, j):
    q = deque()
    q.append([i,j, 1])
    visited[i][j] = 1

    while q:
        cur = q.popleft()
        mmap[cur[0]][cur[1]] = cur[2]

        if cur[0] == N-1 and cur[1] == M-1:
            break

        for dir in range(4):
            ni = cur[0] + di[dir]
            nj = cur[1] + dj[dir]
            
            if ni >= 0 and ni < N and nj >= 0 and nj < M:
                if visited[ni][nj] == 0 and mmap[ni][nj] == 1:
                    visited[ni][nj] = 1
                    q.append([ni,nj, cur[2] + 1])
        
bfs(0, 0)

print(mmap[N-1][M-1])
