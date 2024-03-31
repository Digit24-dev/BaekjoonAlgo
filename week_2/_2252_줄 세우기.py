import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    q = deque()
    ret = []

    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        cur = q.popleft()
        ret.append(cur)

        for i in graph[cur]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    for i in ret:
        print(i, end=' ')

topology_sort()