import sys
input = sys.stdin.readline

N, S = list(map(int, input().split()))
arr = list(map(int, input().split()))
visited = [False] * N

cnt = 0

# 제출
def dfs(numIdx, sum):
    global cnt
    if sum == S:
        cnt += 1
        return

    for i in range(numIdx, N):
        if visited[i] == False:
            visited[i] = True
            dfs(i, sum + arr[i])
            visited[i] = False

for i in range(N):
    visited[i] = True
    # dfs(i, arr[i])
    
    visited[i] = False

ans = []

# 다시 풀기
def solve(start):
    global cnt
    if sum(ans) == S and len(ans) > 0:
        cnt += 1
    for i in range(start, N):
        ans.append(arr[i])
        solve(i + 1)
        ans.pop()

# dfs(0, arr[0])
solve(0)

print(cnt)