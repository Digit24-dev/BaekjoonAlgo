import sys
import copy
from collections import deque

input = sys.stdin.readline

N = int(input())
# graph = [list(map(int, input().strip())) for _ in range(N)]
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for i in range(N):
    line = list(map(int, input().strip()))
    for j in range(N):
        if line[j] == 1:
            graph[i + 1].append(j + 1)
            indegree[j + 1] += 1

print(graph)
print(indegree)

q = deque()

indegree_heap = copy.deepcopy(indegree)
heap = []
result = []
result_heap = []

# 진입 차수가 0인 정점 탐색
for i in range(1, N + 1):
    if indegree_heap[i] == 0:
        q.append(i)
        # heapq.heappush(heap, i)
        result.append(i)

# while heap:
#     cur = heapq.heappop(heap)
#     result_heap.append(cur)

#     for i in graph[cur]:
#         indegree_heap[i] -= 1
#         if indegree_heap[i] == 0:
#             heapq.heappush(heap, -i)

# print(result_heap)           
answer = [0] * (N + 1)

while q:
    cur = q.popleft()
    # result.append(cur)
    
    for i in graph[cur]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)
            result.append(i)

print(result)

for i in range(1, N + 1):
    answer[result[i - 1]] = i

for i in range(1, N + 1):
    print(answer[i], end=' ')
