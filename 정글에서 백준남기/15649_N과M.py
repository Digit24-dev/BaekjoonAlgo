import sys
input = sys.stdin.readline

N, M = map(int, input().split())

visited = [False] * (N + 1)

def dfs(arr: list, cnt):
    if cnt == M:
        for i in arr:
            print(i, end=' ')
        print()
        return
    
    for i in range(1, N+1):
        if visited[i]:
            continue
        visited[i] = True
        arr.append(i)
        dfs(arr, cnt + 1)
        visited[i] = False
        arr.pop(-1)

arr = []
dfs(arr, 0)