import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

### 무방향 그래프는 양쪽 모두 등록해주자.
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

answer = 0

def bfs():
    global answer
    q = deque()

    for start in range(1, N + 1):
        if visited[start] == False:
            visited[start] = True
            answer += 1
            q.append(start)
        else:
            continue

        while q:
            cur = q.popleft()

            for i in graph[cur]:
                if visited[i] == False:
                    visited[i] = True
                    q.append(i)
            
bfs()

print(answer)
