import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
Apart = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
queue = deque()


# 1일때만 타고 가는 dfs로 짜야 할듯;;
# 아래 코드는 0일때도 세는 .. 코드
# 조건 추가 안해줌...

def bfs(graph, x, y):
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        visited[x][y] += 1
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = graph[x][y]

bfs(Apart, 0, 0)
print(*visited)
# for i in range(max(Apart)):