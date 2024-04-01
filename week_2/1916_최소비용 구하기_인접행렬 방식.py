from collections import deque
import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

N = int(input())
M = int(input())
graph = [[INF] * (N + 1) for _ in range(N + 1)]
distances = [INF] * (N + 1)

for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a][b] = cost

start, destination = map(int, input().split())

def debug():
    for i in range(1, N+1):
        for j in range(1, N+1):
            print(graph[i][j], end=' ')
        print()

def dijkstra(s):
    q = []
    distances[s] = 0

    heapq.heappush(q, (0, s))

    while q:
        dist, cur = heapq.heappop(q)
        
        if dist > distances[cur]:
            continue
        
        for i in range(1, N + 1):
            if  graph[cur][i] != INF:
                cost = graph[cur][i]
                new_distance = dist + cost
                if new_distance < distances[i]:
                    heapq.heappush(q, (new_distance, i))
                    distances[i] = new_distance

dijkstra(start)

print(distances[destination])
