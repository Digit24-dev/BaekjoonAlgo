from collections import deque
import sys
input = sys.stdin.readline

K = int(input())

def solve():
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    painted = [0] * (V + 1)

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # # 모든 정점에서 탐색 시작
    # for i in range(1, V + 1):
    #     if visited[i]:
    #         continue

    #     q = deque()
    #     q.append(i)
    #     visited[i] = 1
    #     painted[i] = 0

    #     while q:
    #         cur = q.popleft()
    #         toPaint = (painted[cur] + 1) % 2

    #         for next in graph[cur]:
    #             if visited[next] == 0:
    #                 visited[next] = 1
    #                 painted[next] = toPaint
    #                 q.append(next)
    #             elif painted[next] == painted[cur]:
    #                 return 'NO'
        
    #     return 'YES'


    # 정답 코드
    for i in range(1, V + 1):
        if visited[i]:
            continue

        visited[i] = 1
        q = deque()
        q.append(i)
        while q:
            cur = q.popleft()
            next_color = visited[cur] % 2 + 1

            for next in graph[cur]:
                if visited[next] == 0:
                    visited[next] = next_color
                    q.append(next)
                elif visited[next] != next_color:
                    return 'NO'
        return 'YES'

while K > 0:
    K -= 1
    print(solve())
    