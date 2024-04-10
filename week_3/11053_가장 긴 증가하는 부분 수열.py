import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
max_val = max(arr)

dp = [[0] * (N + 1) for _ in range(1001)]

for i in range(max_val + 1):
    for j in range(len(arr)):
        if arr[j] == i:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# for i in range(max_val + 1):
#     for j in range(len(arr)):
#         print(dp[i][j], end=' ')
#     print()

print(dp[max_val][len(arr) - 1])