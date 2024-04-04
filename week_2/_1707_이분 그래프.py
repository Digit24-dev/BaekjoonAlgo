from collections import deque
import sys
input = sys.stdin.readline

K = int(input())

def solve():
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [False] * (V + 1)
    painted = [0] * (V + 1)

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for startNode in range(1, V + 1):
        if visited[startNode] == True:
            continue

        q = deque()
        q.append(startNode)
        visited[startNode] = True
        painted[startNode] = 0

        while q:
            cur = q.popleft()
            toPaint = (painted[cur] + 1) % 2

            for next in graph[cur]:
                if visited[next] == 0:
                    visited[next] = True
                    painted[next] = toPaint
                    q.append(next)
                elif painted[next] != toPaint:
                    return 'NO'
        
    return 'YES'


while K > 0:
    K -= 1
    print(solve())
    