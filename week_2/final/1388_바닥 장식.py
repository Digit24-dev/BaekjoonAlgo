import sys
input = sys.stdin.readline

N, M = map(int, input().split())

visited = [[False] * (M) for _ in range(N)]
board = [list(input().strip()) for _ in range(N)]

ddi = [1, -1]
ddj = [0,  0]

sdi = [0,  0]
sdj = [1, -1]

answer = 0

def dfs(i, j, tile):
    if tile == '-':
        for dir in range(2):
            ni = i + sdi[dir]
            nj = j + sdj[dir]
            
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == False:
                if board[ni][nj] == tile:
                    visited[ni][nj] = True
                    dfs(ni, nj, tile)
    elif tile == '|':
        for dir in range(2):
            ni = i + ddi[dir]
            nj = j + ddj[dir]
            
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == False:
                if board[ni][nj] == tile:
                    visited[ni][nj] = True
                    dfs(ni, nj, tile)

for i in range(N):
    for j in range(M):
        if visited[i][j] == False:
            answer += 1
            dfs(i, j, board[i][j])

print(answer)