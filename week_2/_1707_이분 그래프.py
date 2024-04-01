from collections import deque
import heapq
import sys
input = sys.stdin.readline

K = int(input())

def dfs(g, start, visited, c):
    visited[start] = True
    toPaint = not c

    for idx in range(len(g[start])):
        i = g[start][idx][0]
        
        if visited[i] == False:
            g[start][idx][1] = toPaint
            dfs(g, i, visited, toPaint)
        else:
            if g[start][idx][1] == toPaint:
                return 'NO'

    return 'YES'

def bfs(graph, s, visited):
    q = deque()
    q.append((s, 0))
    visited[s] = True

    while q:
        cur, color = q.popleft()
        color += 1

        for i in graph[cur]:
            if visited[i[0]] == False:
                visited[i[0]] = True
                q.append((i[0], color))
            else:
                print(type(graph[i[0]]), graph[i[0]])
                # if graph[i[0]][1] & 0x01 == color & 0x01:
                #     return 'no'
    return 'yes'


    # print(graph)

def solve():
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

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
    