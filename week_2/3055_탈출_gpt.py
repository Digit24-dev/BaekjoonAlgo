from collections import deque

WATER = '*'
GOSUM = 'S'
ROCK = 'X'
HOUSE = 'D'
BLANK = '.'

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
waters = deque()
gosum = deque()

# 비버 굴, 고슴도치 위치, 물 위치 등록하기
for i in range(R):
    for j in range(C):
        if board[i][j] == GOSUM:
            gosum.append((i, j, 0))  # 고슴도치의 초기 위치와 시간(0)을 저장
        elif board[i][j] == WATER:
            waters.append((i, j))

def spread_water():
    while waters:
        i, j = waters.popleft()
        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if 0 <= ni < R and 0 <= nj < C and board[ni][nj] == BLANK:
                board[ni][nj] = WATER
                waters.append((ni, nj))

def move_gosum():
    while gosum:
        i, j, time = gosum.popleft()
        if board[i][j] == HOUSE:  # 고슴도치가 비버 굴에 도착한 경우
            return time
        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if 0 <= ni < R and 0 <= nj < C and (board[ni][nj] == BLANK or board[ni][nj] == HOUSE):
                board[ni][nj] = GOSUM
                gosum.append((ni, nj, time + 1))  # 고슴도치의 새로운 위치와 시간을 큐에 추가
    return -1  # 비버 굴에 도착하지 못한 경우

def solve():
    time = 0
    while gosum:
        spread_water()  # 물이 퍼지는 것을 먼저 처리
        res = move_gosum()  # 고슴도치 이동
        if res != -1:
            return res
        time += 1
    return -1  # 고슴도치가 비버 굴에 도착하지 못한 경우

result = solve()
if result == -1:
    print("KAKTUS")
else:
    print(result)
