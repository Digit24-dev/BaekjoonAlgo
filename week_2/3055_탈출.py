import sys
from collections import deque
input = sys.stdin.readline

WATER = '*'
GOSUM = 'S'
ROCK = 'X'
HOUSE = 'D'
BLANK = '.'

def debug():
    for i in range(R):
        for j in range(C):
            print(board[i][j], end=' ')
        print()

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

R, C = map(int, input().split())
board = [[] for _ in range(R)]
flag = True

for i in range(R):
    board[i] = list(input().strip())

# 비버 굴, 고슴도치 위치, 물 위치 등록하기
# 물 위치는 큐에 넣고 빼면서 바뀐 위치들을 큐에 넣을 것.
waters = deque()
gosum = deque()

visited_waters = [[False] * (C) for _ in range(R)]
visited_gosum = [[False] * (C) for _ in range(R)]

for i in range(R):
    for j in range(C):
        c = board[i][j]
        if c == GOSUM:
            gosum.append((i,j))
            visited_gosum[i][j] = True

        elif c == WATER:
            waters.append((i,j))
            visited_waters[i][j] = True

        elif c == HOUSE:
            housePos = (i,j)

def watering():
    n = len(waters)

    while n:
        n -= 1
        i, j = waters.popleft()
        
        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]

            if 0 <= ni < R and 0 <= nj < C and visited_waters[ni][nj] == False:
                if board[ni][nj] is not HOUSE and board[ni][nj] is not ROCK:
                    visited_waters[ni][nj] = True
                    board[ni][nj] = WATER
                    waters.append((ni, nj))

time = 0
endFlag = False

while True:
# while input():
    time += 1
    movedFlag = True

    # 물 확장
    watering()
    
    # 고슴도치 이동
    g = len(gosum)
    while g:
        g -= 1
        i, j = gosum.popleft()

        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]

            if 0 <= ni < R and 0 <= nj < C and visited_gosum[ni][nj] == False:
                if board[ni][nj] == BLANK:
                    visited_gosum[ni][nj] = True
                    board[ni][nj] = time
                    gosum.append((ni, nj))
                    movedFlag = False
                
                if board[ni][nj] == HOUSE:
                    # print(time)
                    endFlag = True
                    movedFlag = False
                    break
    
    if movedFlag:
        # print('KAKTUS')
        break

    # debug()
    if endFlag: break

if movedFlag:
    print('KAKTUS')
else:
    print(time)