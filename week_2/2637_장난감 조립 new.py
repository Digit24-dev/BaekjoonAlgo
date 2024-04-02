import sys
from collections import deque
input = sys.stdin.readline

# 입력 BEGIN
N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
basic_parts = [0] * (N + 1)

for _ in range(M):
    X, Y, K = map(int, input().split())
    graph[X].append((Y, K))
    indegree[Y] += 1
# 입력 END

# 기본 부품 등록
basic_parts_list = []
for i in range(1, N + 1):
    if len(graph[i]) == 0:
        basic_parts_list.append(i)
# 기본 부품 등록 END

# print(graph)
# print(indegree)
# print(basic_parts)

# topology sort
def topology_sort():
    q = deque()
    result = []

    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
            # 진입 차수가 0 인 것들이 기본 부품이다.

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

for i in sorted_result:
    for idx, cnt in graph[i]:
        if basic_parts[i] == 0:
            basic_parts[idx] += cnt
        else:
            basic_parts[idx] += cnt * basic_parts[i]

for i in basic_parts_list:
    print(i, basic_parts[i])
