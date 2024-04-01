import sys
import heapq
input = sys.stdin.readline

M, N = map(int, input().split())

di = [1,0,-1,0]
dj = [0,1,0,-1]

board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip())))

visited = [[0] * M for _ in range(N)]

# for i in range(N):
#     for j in range(M):
#         print(board[i][j], end='')
#     print()

def bfs():
    heap = []
    heapq.heappush(heap, [0, 0, 0])
    visited[0][0] = 1

    while heap:
        a, i, j = heapq.heappop(heap)

        # 끝점 도착시에 종료 시킴.
        if i == N - 1 and j == M - 1:
            print(a)
            return
        
        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]

            # 방향 갱신 및 방문 여부 확인
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                # 벽(1)일 경우 현재 위치 (ni, nj)를 진행시키며, 맨 앞의 가중치를 업데이트 시킨다.
                # 최소 힙큐를 활용하면, 가중치가 가장 낮은 순서대로 정렬되므로 
                # 힙에 정렬된 제일 낮은 가중치의 값이 pop된다.
                if board[ni][nj] == 1:
                    heapq.heappush(heap, [a+1, ni, nj])
                else:
                    heapq.heappush(heap, [a, ni, nj])
                # 방문 처리
                visited[ni][nj] = 1

bfs()

