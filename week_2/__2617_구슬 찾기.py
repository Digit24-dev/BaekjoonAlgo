import sys
from collections import deque
from itertools import combinations, permutations
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    indegree[v] += 1

# 1. 위상 정렬로 먼저 풀어보자.
print(graph)
print(indegree)

q = deque()
# combination = [list(combinations(q, 1))]
combination = []

for i in range(1, N + 1):
    if indegree[i] == 0:
        # q.append(i)
        combination.append(i)

topsorted = []
c = list(combinations(combination, 1))
print(c)

for q, in combination:
    while q:
        cur = q.popleft()
        topsorted.append(cur)

        for i in graph[cur]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    print(topsorted)