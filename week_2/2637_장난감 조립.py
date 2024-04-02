import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
basic_parts = [0] * (N + 1)

for _ in range(M):
    X, Y, K = map(int, input().split())
    graph[Y].append((X, K))
    indegree[X] += 1
    
print(graph)
print(indegree)

# topology sort
def topology_sort():
    q = deque()
    result = []

    for i in range(1, N + 1):
        if indegree[i] == 0:
            # 진입 차수가 0 인 것들이 기본 부품이다.
            q.append(i)

    while q:
        cur = q.popleft()
        result.append(cur)

        for node in graph[cur]:
            next, cnt = node
            indegree[next] -= 1

            if indegree[next] == 0:
                q.append(next)
    
    return result

sorted_result = topology_sort()

for i in range(N - 1, -1, -1):
    for node in graph[i]:
        basic_parts[node[0]] += node[1]

    print(sorted_result[i], end=' ')
