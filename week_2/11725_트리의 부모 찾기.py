import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
parents = [0] * (N + 1)

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parents[1] = 1
visited[1] = True

def dfs(s):
    visited[s] = True

    for i in graph[s]:
        if visited[i] == False:
            parents[i] = s
            dfs(i)

dfs(1)

for i in range(2, N + 1):
    print(parents[i])