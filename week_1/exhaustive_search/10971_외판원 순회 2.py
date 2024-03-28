import sys
import queue
input = sys.stdin.readline

N = int(input())
visited = [False] * N

def debug() -> None:
    for i in range(N):
        for j in range(N):
            print(mmap[i][j], end=' ')
        print()

mmap = [[0] * N for _ in range(N)]

# input
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        mmap[i][j] = line[j]

# debug()

def dfs(start, cur, cost, depth):
    global answer

    if depth == N:
        if mmap[cur][start] != 0:
            cost += mmap[cur][start]
            answer = min(answer, cost)
        return
    
    for k in range(N):
        if visited[k] == False and mmap[cur][k] != 0 and k != start:
            visited[k] = True
            cost += mmap[cur][k]
            
            dfs(start, k, cost, depth + 1)

            visited[k] = False
            cost -= mmap[cur][k]

answer = sys.maxsize

# i -> j
for i in range(N):
    visited[i] = True
    dfs(i, i, 0, 1)
    visited[i] = False

print(answer)

# bfs 로도 풀어보기

# q = queue.Queue()
# def bfs():
#     # 탐색 - bfs
#     shouldBeLast = i
#     q.put([i, j])
#     tempAns = 0
#     visitCnt = 0

#     while not q.empty():
#         cur = q.get()
#         print(cur[0], '->',cur[1], '방문함')
#         visitCnt += 1
#         lastVisit = cur[1]
#         tempAns += mmap[cur[0]][cur[1]]
#         # mmap[cur[0]][cur[1]] = 0
#         # visited[cur[1]] = True

#         for k in range(N):
#             if visited[k] == False and mmap[cur[1]][k] != 0 and k != shouldBeLast:
#                 q.put([cur[1], k])
#                 visited[k] = True
        
#     # bfs end
#     if visitCnt > 3 and mmap[lastVisit][shouldBeLast] != 0:
#         tempAns += mmap[lastVisit][shouldBeLast]
#         answer = min(answer, tempAns)
    
#     print('============')
#     # answer = min(answer, tempAns)
    
#     # backtrack
#     visited = [False] * N
#     # mmap = cmmap