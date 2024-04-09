import sys

input = sys.stdin.readline

def mulMatrix(a: tuple, b: tuple):
    return a[0] * a[1] * b[1], (a[0], b[1])

N = int(input())
visited = [0] * (N)

matrixes = []

for i in range(N):
    r, c = map(int, input().split())
    matrixes.append((r,c))

print(matrixes)

for i in range(len(matrixes) - 1):
    data, ret = mulMatrix(matrixes[i], matrixes[i+1])

arr = []

def dfs(cnt):
    if cnt == N:
        print(arr)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            arr.append(i)
            dfs(cnt + 1, i)
            visited[i] = False
            arr.pop()

dfs(0, 0)