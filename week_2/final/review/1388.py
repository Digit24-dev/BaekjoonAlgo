import sys
input = sys.stdin.readline

N, M = map(int, input().split())
floor = [list(input().strip()) for _ in range(N)]
visited = [[False] * (M + 1) for _ in range(N + 1)]


# 왜 안되는지 도저히 모르겠음... 계속 0이 나옴
def dfs(graph, x, y):
    visited[x][y] = True
    count = 1

    if graph[x][y] == '-':
        for dx in 1, -1:
            if not visited[dx + x][y] and 0 <= dx + x < N and 0 <= y < N:
                visited[dx + x][y]
                count += dfs(graph, dx + x, y)

    if graph[x][y] == '|':
        for dy in 1, -1:
            if not visited[x][dy + y] and 0 <= dy + y < N and 0 <= x < N:
                count += dfs(graph, x, dy + y)

    return count

print(dfs(floor, 0, 0))