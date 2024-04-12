import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def top_down(n,dp,continuous):
    global stair

    if continuous > 3:
        return 0

    if n <= 1 or dp[n]:
        return dp[n]

    if n <= 2:
        if continuous + 1 <= 2:
            one_step = top_down(n-1, dp,continuous+1)
            dp[n] = stair[n] + top_down(n-1, dp, continuous+1)
    else:
        one_step, two_step = 0, 0
        if continuous + 1 <= 2:
            one_step =top_down(n-1, dp,continuous+1)
        two_step =top_down(n-2, dp,1)
        dp[n] = max(one_step,two_step) + stair[n]

    return dp[n]

N = int(input())
stair = [0] * (N + 1)
dp = [0] * (N + 1)
for i in range(1, N+1):
    floor = int(input())
    stair[i] = floor

dp[1] = stair[1]
continuous = 1

print(top_down(N,dp,continuous))