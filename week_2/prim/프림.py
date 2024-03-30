import heapq as hq

def prim(start):
    heap = list()
    # 연결되어 있는지 확인하는 리스트
    connected = [False] * (NODE_CNT + 1)

    sum_w = 0
    hq.heappush(heap, (0, start))

    print('Minimum Spanning Tree')

    # 우선순위 큐에 데이터가 있는 동안
    while heap:
        weight, v = hq.heappop(heap)
        # 뺀 노드가 그래프에 포함되어 있지 않은 경우
        if not connected[v]:
            # 그래프에 포함 처리
            connected[v] = True
            sum_w += weight
            print('Connected Nodes: ', v, 'Weight: ', weight)
            for i in range(1, NODE_CNT + 1):
                if graph[v][i] != 0 and not connected[i]:
                    hq.heappush(heap, (graph[v][i], i))
    
    print('Sum of weight: ', sum_w)


if __name__ == "__main__":
    NODE_CNT = 5
    graph = [[0] * (NODE_CNT + 1) for _ in range(NODE_CNT + 1)]
    root = list(range(NODE_CNT + 1))
    graph[1][2], graph[1][3], graph[1][4] = 1, 8, 3
    graph[2][1], graph[2][4], graph[2][5] = 1, 2, 7
    graph[4][1], graph[4][2], graph[4][3], graph[4][5] = 3, 2, 4, 6
    graph[5][2], graph[5][3], graph[5][4] = 7, 5, 6

    prim(1)