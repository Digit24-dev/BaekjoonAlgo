import heapq
import collections
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = collections.defaultdict(list)   # 빈 그래프 생성
visited = [0] * (n + 1)

# 무방향 그래프
for i in range(m):
    u, v, weight = map(int, input().split())
    graph[u].append([weight, u, v])
    graph[v].append([weight, v, u])

def myPrim(graph, start):
    mst = []
    total_weight = 0
    visited[start] = True
    q = graph[start]
    
    heapq.heapify(q)
    
    while q:
        w, u, v = heapq.heappop(q)
        mst.append((u, v))

        if visited[v] == 0:
            total_weight += w
            visited[v] = 1
            mst.append((u, v))

            for next in graph[v]:
                if visited[next[2]] == 0:
                    heapq.heappush(q, next)

    return total_weight
        
# 프림 알고리즘
def prim(graph, start):
    visited[start] = 1
    q = graph[start]
    heapq.heapify(q)
    mst = []
    total_weight = 0

    while q:
        weight, u, v = heapq.heappop(q)
        
        if visited[v] == 0:
            total_weight += weight
            visited[v] = 1
            mst.append((u, v))

            for next in graph[v]:
                if visited[next[2]] == 0:
                    heapq.heappush(q, next)
    
    return total_weight

print(prim(graph, 1))