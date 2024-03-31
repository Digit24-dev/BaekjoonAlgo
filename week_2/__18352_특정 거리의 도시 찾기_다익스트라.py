import heapq
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
INF = int(1e9)

graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    
def dijkstra(start):
    distance[start] = 0
    q = []
    #### !!!! 우선 순위 큐를 사용할 떄에는 튜플의 최초항 기준 정렬되므로 순서에 유의하자.
    heapq.heappush(q, (0, start))   
    
    while q:
        dist, cur = heapq.heappop(q)
        if distance[cur] < dist:
            continue
        for i in graph[cur]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                heapq.heappush(q, (cost, i[0]))
                distance[i[0]] = cost

dijkstra(X)

ret = []
for i in range(1, N + 1):
    if distance[i] == K:
        ret.append(i)

if ret:
    for i in ret:
        print(i, end='\n')
else:
    print(-1)