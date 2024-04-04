import sys
from collections import deque
import heapq

input = sys.stdin.readline

INF = int(1e9)

# 다익스트라 역순?
# bfs로 cost, 간선정보 가져오기

n = int(input())
m = int(input())
graph = [[] * (n+1) for _ in range(n + 1)]
back_graph = [[] * (n+1) for _ in range(n+1)]
indegree = [0]* (n+1)
result = [0] * (n+1)
check = [0] * (n+1)
q = deque()
for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    back_graph[b].append((a, t))
    indegree[b] += 1
start, end = map(int, input().split())

q.append(start)
def topology_sort():
    while q:
        cur = q.popleft()
        for i, t in graph[cur]:
            indegree[i] -= 1
            result[i] = max(result[i], result[cur] + t)
            if indegree[i] == 0:
                q.append(i)

    # 백트래킹
    cnt = 0
    q.append(end)
    while q:
        cur = q.popleft()
        for i, t in back_graph[cur]:

            if result[cur] - result[i] == t:
                cnt += 1
                if check[i] == 0:
                    q.append(i)
                    check[i] = 1
    print(result[end])
    print(cnt)
    
topology_sort()
