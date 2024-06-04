import sys
import heapq

input = sys.stdin.readline

# 인접 리스트 형태의 그래프
graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

# 인접 리스트 형태의 그래프 다익스트라로 최단 경로의 비용 구하기
def daijkstra(start):
    INF = int(1e9)
    distances = {node: INF for node in graph}
    distances[start] = 0
    q = []

    heapq.heappush(q, (0, start))

    while q:
        dist, cur = heapq.heappop(q)

        if dist > distances[cur]:
            continue

        for nextNode, newCost in graph[cur].items():
            new_dist = dist + newCost
            if new_dist < distances[nextNode]:
                distances[nextNode] = new_dist
                heapq.heappush(q, (new_dist, nextNode))

    return distances

ret = daijkstra('C')

print(ret)