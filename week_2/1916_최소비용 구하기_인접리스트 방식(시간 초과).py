from collections import deque
import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
distances = [INF] * (N + 1)

for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

start, destination = map(int, input().split())

def dijkstra(s):
    q = []
    distances[s] = 0

    for i in graph[s]:
        heapq.heappush(q, (i[1], i[0]))

    while q:
        dist, cur = heapq.heappop(q)
        
        if dist > distances[cur]:
            continue
        
        for node in graph[cur]:
            new_dist = dist + node[1]
            if new_dist < distances[node[0]]:
                heapq.heappush(q, (new_dist, node[0]))
                distances[node[0]] = new_dist

dijkstra(start)

print(distances[destination])
