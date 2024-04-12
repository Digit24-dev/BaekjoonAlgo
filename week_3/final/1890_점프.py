import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

di = [1, 0]
dj = [0, 1]

dp = [[0] * (N) for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if graph[i][j] == 0: break

        for dd in range(2):
            ni = i + (graph[i][j] * di[dd])
            nj = j + (graph[i][j] * dj[dd])

            if 0 <= ni < N and 0 <= nj < N:
                # (0, 0)부터 해당 위치까지 가는 방법 수를 더했으므로... 이게 맞다...
                dp[ni][nj] += dp[i][j]
                # dp[ni][nj] += 1

for k in range(N):
    for m in range(N):
        print(dp[k][m], end=' ')
    print()

print(dp[N-1][N-1])
