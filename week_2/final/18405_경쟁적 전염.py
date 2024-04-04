import sys
from collections import deque
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

S, X, Y = map(int, input().split())

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def debug():
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()

def bfs():
    # spread virus
    q = []

    # 0이 아닐 경우 힙 푸시
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                # 바이러스 종류, i, j
                heapq.heappush(q, (board[i][j], i, j))
    
    while q:
        virus, ci, cj = heapq.heappop(q)

        for dir in range(4):
            ni = ci + di[dir]
            nj = cj + dj[dir]

            if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == 0:
                board[ni][nj] = virus

flag = True
time = 0
while time <= S:
# while input():
    # 위치 값 확인
    if board[X - 1][Y - 1] != 0:
        print(board[X - 1][Y - 1])
        flag = False
        break

    time += 1
    # 바이러스 퍼짐
    bfs()

if flag:
    print(0)