import sys
from collections import deque
import copy
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * (M) for _ in range(N)]

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def debug(board=board):
    for i in range(N):
        for j in range(M):
            print(board[i][j], end=' ')
        print()

def melting():
    global board
    copyBoard = copy.deepcopy(board)

    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                continue

            c = meltToCNT(i, j)

            if board[i][j] - c < 0:
                copyBoard[i][j] = 0
            else:
                copyBoard[i][j] -= c

    board = copy.deepcopy(copyBoard)

def meltToCNT(i, j):
    cnt = 0
    for dir in range(4):
        ni = i + di[dir]
        nj = j + dj[dir]

        if 0 <= ni < N and 0 <= nj < M and board[ni][nj] == 0:
            cnt += 1
    
    return cnt

def isDone():  # bfs
    searchedOne = False
    isSeperated = False

    q = deque()
    visited = [[False] * (M) for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if board[i][j] == 0 or visited[i][j]:
                continue

            if searchedOne:
                isSeperated = True
                break

            q.append((i, j))
            visited[i][j] = True

            while q:
                ci, cj = q.popleft()

                for dir in range(4):
                    ni = ci + di[dir]
                    nj = cj + dj[dir]

                    if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and board[ni][nj] != 0:
                        visited[ni][nj] = True
                        q.append((ni, nj))
            
            searchedOne = True
    
    return isSeperated, searchedOne

year = 0
while True:
# while input():
    year += 1

    # 눈 녹이기
    melting()

    # debug()

    # 빙산 분리 됬는지 확인하기
    isSeperated, searchedOne = isDone()

    if isSeperated:
        print(year)
        break
    
    if not searchedOne:
        print(0)
        break




'''
5 5
0 0 0 0 0
0 1 1 1 0
0 1 0 1 0
0 1 1 1 0
0 0 0 0 0

0


4 4
0 0 0 0
0 3 1 0
0 1 3 0
0 0 0 0

1

5 7
0 0 0 0 0 0 0
0 3 3 2 3 3 0
0 4 0 4 0 3 0
0 0 0 0 4 3 0
0 0 0 0 0 0 0

0
'''