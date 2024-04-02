import heapq
INF = int(1e9)

graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

# ####### 연결 리스트 형태의 다익스트라 ############
# def dijkstra(graph, start):
#     distances = {node: float('inf') for node in graph}      # start로 부터의 거리 값을 저장하기 위함
#     distances[start] = 0
#     queue = []
#     heapq.heappush(queue, [distances[start], start])        # 파이썬은 최소 힙. - 시작 노드부터 탐색 시작하기 위함.

#     while queue:               # 큐에 남아 있는 노드가 없으면 끝
#         current_distance, current_destination = heapq.heappop(queue)        # 탐색할 노드, 거리를 가져옴

#         if distances[current_destination] < current_distance:               # 기존에 있는 거리보다 길다면, 튕굼
#             continue

#         for new_destination, new_distance in graph[current_destination].items():
#             distance = current_distance + new_distance
#             if distance < distances[new_destination]:
#                 distances[new_destination] = distance
#                 heapq.heappush(queue, [distance, new_destination])          # 다음 인접 거리를 계산하기 위해 큐에 삽입

#     return distances

####### 행렬 형태의 다익스트라 ##############
def dijkstra(graph, start):
    distances = [INF for _ in range(N + 1)]
    distances[start] = 0

    q = []
    heapq.heappush(q, [distances[start], start])

    while q:
        cur_distance, cur_destination = heapq.heappop(q)
        
        if cur_distance > distances[cur_destination]:
            continue
        
        for new_destination in range(1, N + 1):
            if graph[cur_destination][new_destination] == 1:
                new_distance = cur_distance + 1
                if new_distance < distances[new_destination]:
                    distances[new_destination] = new_distance
                    heapq.heappush(q, [new_distance, new_destination])

    return distances


print(dijkstra(graph, 'C'))