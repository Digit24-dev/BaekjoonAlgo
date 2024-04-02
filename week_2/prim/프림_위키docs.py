import heapq

def prim(graph, start):
    mst = [] # 결과 트리
    visited = set() # 방문 여부를 저장하는 집합
    edges = [] # 우선 순위 큐
    count = 0
    cost = 0

    # 시작 노드를 우선순위 큐에 추가
    heapq.heappush(edges, (0, start))

    # 이동 가능한 노드가 없거나 모든 노드를 방문하여 이용한
    # 간선의 갯수가 v - 1 이 될 때까지 반복한다.
    while edges and count < len(graph) - 1:
        # 가장 가중치가 작은 edge 선택
        w, node = heapq.heappop(edges)
        
        # 이미 방문한 노드는 건너뛴다.
        if node not in visited:
            cost += w
            count += 1
            
            # 방문하지 않은 노드라면 결과 트리에 추가
            visited.add(node)
            mst.append((node, w))
            
            # 현재 노드와 연결된 에지를 우선순위 큐에 추가
            for edge, w in graph[node].items():
                heapq.heappush(edges, (w, edge))
        
    # 고립 노드 존재시 모두 연결할 수 없으므로 체크
    if count == len(graph) - 1:
        return mst, cost
    return False

if __name__ == "__main__":
    # 그래프 정의 (노드와 가중치)
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    # 프림 알고리즘 실행
    result = prim(graph, 'A')
    print(result)
