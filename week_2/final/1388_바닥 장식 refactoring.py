import sys
input = sys.stdin.readline

N, M = map(int, input().split())

visited = [[False] * (M) for _ in range(N)]
board = [list(input().strip()) for _ in range(N)]

ddj = [1, -1]
ddi = [0,  0]

sdj = [0,  0]
sdi = [1, -1]

answer = 0

def dfs_s(i, j):
    for dir in range(2):
        ni = i + sdi[dir]
        nj = j + sdj[dir]

        if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == False:
                if board[ni][nj] == '|':
                    visited[ni][nj] = True
                    dfs_s(ni, nj)

def dfs_d(i, j):
    for dir in range(2):
        ni = i + ddi[dir]
        nj = j + ddj[dir]

        if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == False:
                if board[ni][nj] == '-':
                    visited[ni][nj] = True
                    dfs_d(ni, nj)

for i in range(N):
    for j in range(M):
        if visited[i][j] == False:
            visited[i][j] = True
            answer += 1
            if board[i][j] == '-':
                dfs_d(i,j)
            else:
                dfs_s(i,j)

print(answer)