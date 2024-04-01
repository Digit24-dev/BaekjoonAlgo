from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
INF = int(1e9)

graph = [[0] for _ in range(N + 1)]
visited = [False] * (N + 1)
visited[0] = True

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(graph, start):
    dist = 0
    ret = []

    q = deque()
    q.append([start, dist])
    visited[start] = True

    while q:
        cur, cur_dist = q.popleft() 
        # print(cur, cur_dist)
        for i in graph[cur]:
            if visited[i] == False:
                visited[i] = True
                # print(cur, i, cur_dist)
                q.append([i, cur_dist + 1])
                if cur_dist + 1 == K:
                    ret.append(i)
    return ret

result = bfs(graph, X)
if result:
    result.sort()
    for i in result:
        print(i)
else:
    print(-1)