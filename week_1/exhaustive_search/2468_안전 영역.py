import sys
import queue
from collections import deque

# -> deque 으로 다시 풀어보기

input = sys.stdin.readline

N = int(input())
mmap = [[0] * N for _ in range(N)]

maximum_h = 0

max_safeHouse = 0

visited = [[False] * N for _ in range(N)]

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def isRange(i, j):
    return i >= 0 and i < N and j >= 0 and j < N

# input
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        mmap[i][j] = line[j]
        maximum_h = max(maximum_h, line[j])

def bfs(i, j, h):
    q = queue.Queue()
    q.put([i,j])
    visited[i][j] = True

    while not q.empty():
        # debug()
        cur = q.get()

        for dir in range(4):
            ni = cur[0] + di[dir]
            nj = cur[1] + dj[dir]

            if ni >= 0 and ni < N and nj >= 0 and nj < N:
                if visited[ni][nj] == False and  mmap[ni][nj] > h:
                    q.put([ni, nj])
                    visited[ni][nj] = True
        

for h in range(maximum_h):
    # 준비
    cnt = 0
    # 탐색 시작
    for i in range(N):
        for j in range(N):
            if mmap[i][j] > h and not visited[i][j]:
                cnt += 1
                bfs(i, j, h)
                # max safeHouse 갱신
    # max_safeHouse.append([cnt, h])
    max_safeHouse = max(max_safeHouse, cnt)
    visited = [[False] * N for _ in range(N)]

print(max_safeHouse)