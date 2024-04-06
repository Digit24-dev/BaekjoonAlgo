import sys
input = sys.stdin.readline

N, K = map(int, input().split())

Weigths = [0] * (N + 1)
Values = [0] * (N + 1)
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    W, V = map(int, input().split())
    Weigths[i] = W
    Values[i] = V

for i in range(1, N+1):
    for j in range(1, K+1):
        if Weigths[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - Weigths[i]] + Values[i])

print(dp[N][K])

# for i in range(0, N+1):
#     for j in range(0, K+1):
#         print(dp[i][j], end='\t')
#     print()
