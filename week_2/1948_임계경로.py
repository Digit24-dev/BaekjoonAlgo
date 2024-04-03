import sys
from collections import deque
import heapq

input = sys.stdin.readline

INF = int(1e9)

# 다익스트라 역순?
# bfs로 cost, 간선정보 가져오기

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]

distances = [-INF] * (n + 1)

visited = [False] * (n + 1)
edges = []

for _ in range(m):
    u, v, time_cost = map(int, input().split())
    # time <= 10000
    graph[u].append((v, time_cost))
    # edges.append(time_cost, u, v)

start, end = map(int, input().split())

answer_1 = 0

answer_2 = set()

def bfs(start):
    global answer_1

    q = deque()
    edges_list = []
    q.append((start, 0, edges_list[:]))

    while q:
        cur, cost, ll = q.popleft()
        # print(cur, cost)
        
        for node in graph[cur]:
            v, new_cost = node
            new_cost += cost
            ll.append((cur, v))
            q.append((v, new_cost, ll))

            # answer_1 = max(answer_1, new_cost)
            if new_cost > answer_1:
                answer_1 = new_cost
                # answer_2.add(ll[:])
                
                
                for i in ll:
                    answer_2.add(i)

bfs(start)

for i in answer_2:
    print(i, end=' ')
print()
print(answer_1, len(answer_2))
