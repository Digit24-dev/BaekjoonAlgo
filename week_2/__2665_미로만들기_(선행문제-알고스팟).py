import heapq
import sys
input = sys.stdin.readline

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

N = int(input())
board = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

def dijkstra():
    heap = []
    visited[0][0] = True
    heapq.heappush(heap, [0, 0, 0])

    while heap:
        cost, i, j = heapq.heappop(heap)
        board[i][j] = cost

        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]
            
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == False:
                visited[ni][nj] = True

                if board[ni][nj] == 1:
                    heapq.heappush(heap, [cost, ni, nj])
                else:
                    heapq.heappush(heap, [cost + 1, ni, nj])
    
dijkstra()

print(board[N-1][N-1])