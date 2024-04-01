import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

# 진입 차수
indegree = [0] * (n + 1)
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    # 그래프를 입력하며 진입 차수를 기록함
    indegree[b] += 1

def topology_sort():
    result = []
    queue = deque()

    for i in range(1, n+1):
        
        # 진입 차수가 0인 정점일 경우
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        current = queue.popleft()
        result.append(current)
        
        for i in graph[current]:
            # current로부터 나가는 간선 제거
            indegree[i] -= 1        # 간선 삭제 과정
            if indegree[i] == 0:
                queue.append(i)

    # 출력 : 1 2 3 4 5
    # for i in result:
    #     print(i, end='')
    print(*result)


topology_sort()
print()
