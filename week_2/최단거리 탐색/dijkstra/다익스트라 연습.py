import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
distances = [INF] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)

def dijkstra(start):
    result = []

    distances[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        dist, cur = heapq.heappop(heap)

        if dist > distances[cur]:
            continue

        for i in graph[cur]:
            cost = dist + 1
            if cost < distances[i]:
                distances[i] = cost
                heapq.heappush(heap, (cost, i))

    for i in range(1, N + 1):
        if distances[i] == K:
            result.append(i)
            
    if result:
        result.sort()
        return result
    else:
        return [-1]

ret = dijkstra(X)

for i in ret:
    print(i)