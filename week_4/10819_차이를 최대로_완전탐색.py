import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
visited = [False] * N

a = []
sum = 0

def dfs(cnt):
    global sum

    if cnt >= N:
        temp = 0
        for i in range(0, N - 1):
            temp += abs(a[i] - a[i + 1])
        print(a)
        sum = max(sum, temp)

    for i in range(N):
        if visited[i] == False:
            visited[i] = True
            a.append(arr[i])

            dfs(cnt + 1)

            visited[i] = False
            a.pop()


for i in range(N):
    visited[i] = True
    a.append(arr[i])
    dfs(1)
    visited[i] = False
    a.pop()

print(sum)