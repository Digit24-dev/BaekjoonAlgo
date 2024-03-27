import sys
from dataclasses import dataclass
from collections import deque
input = sys.stdin.readline

def canMove(i, j):
    return i > 0 and i < N + 1 and j > 0 and j < N + 1 and mmap[i][j] != 2

def debug():
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            print(mmap[i][j], ' ', end='')
        print()

############################ INPUT ############################

# 맵 초기화하기
N = int(input())
mmap = [[0] * (N + 1) for _ in range(N + 1)]
# 빈칸 0 / 사과 1 / 뱀 2

# 사과 입력 받기
K = int(input())
for _ in range(K):
    i, j = map(int, input().strip().split())
    mmap[i][j] = 1

mmap[1][1] = 2

# 방향 받기
# [0]초 뒤 [1] 방향 이동
L = int(input())
comm = []
for _ in range(L):
    comm.append(input().strip().split())

########################## END INPUT ##########################

time = 0

arrow = {
    'L' : -1,
    'D' : 1
}

#     R D L U
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# snake info
@dataclass
class Head:
    x: int
    y: int

class Snake:
    def __init__(self) -> None:
        # deque에 0은 head 정보 , len(body)-1 은 tail 정보
        # body에 head와 tail에 대한 정보를 계속 담고 mmap에 그린다
        self.body = deque()
        self.head = Head(1, 1)
        self.body.append([self.head.x, self.head.y])
        self.direction = 0
        # self.tail = Head(1, 1)
        # self.head.x = self.head.y = self.tail.x = self.tail.y = 1

    def move(self):
        self.head.x += dx[self.direction]
        self.head.y += dy[self.direction]

        # 충돌 검사 // 충돌시 0 // 비충돌시 1
        if canMove(self.head.x, self.head.y):
            # 성공
            # 사과일 경우
            if mmap[self.head.x][self.head.y] == 1:
                self.eat(self.head.x, self.head.y)
                mmap[self.head.x][self.head.y] = 2
                return True
            
            # head에 그리고 tail 제거, mmap 에서 빈칸으로 만들기
            self.body.append([self.head.x, self.head.y])
            mmap[self.head.x][self.head.y] = 2
            cord = self.body.popleft()
            mmap[cord[0]][cord[1]] = 0

            return True
        else:
            return False

    def change_dir(self, d):
        self.direction = (4 + self.direction + arrow[d]) % 4

    def eat(self, x, y):
        self.body.append([x, y])

# R D L U
snakeInfo = Snake()

# 게임 시작
# while input():
while True:
    time += 1
        
    # 방향 이동
    if snakeInfo.move() == False:
        break

    # 명령 분석
    if len(comm) > 0 and int(comm[0][0]) == time:
        command = comm.pop(0)
        snakeInfo.change_dir(command[1])

    # debug()
    
print(time)