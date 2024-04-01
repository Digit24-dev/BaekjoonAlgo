from collections import deque
import sys
input = sys.stdin.readline

di = [1, 0, -1, 0, 0, 0]
dj = [0, 1, 0, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

M, N, H = map(int, input().split())

board = [[]] * H
visited = [[[False] * M for _ in range(N)] for _ in range(H)]

for h in range(H):
    board[h] = [list(map(int, input().split())) for _ in range(N)]

def bfs():
    ret = 0
    q = deque()
    
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if board[h][i][j] == 1:
                    visited[h][i][j] = True
                    q.append([i,j,h,0])
    
    while q:
        i, j, h, day = q.popleft()
        
        # in box
        for dir in range(6):
            ni = i + di[dir]
            nj = j + dj[dir]
            nh = h + dh[dir]
            
            if 0 <= ni < N and 0 <= nj < M and 0 <= nh < H and visited[nh][ni][nj] == False:
                if board[nh][ni][nj] == 0:
                    board[nh][ni][nj] = 1
                    visited[nh][ni][nj] = True
                    q.append([ni, nj, nh, day + 1])
                    ret = max(ret, day + 1)


    for h in range(H):
        for i in range(N):
            for j in range(M):
                if board[h][i][j] == 0:
                    return -1
    
    return ret

print(bfs())
