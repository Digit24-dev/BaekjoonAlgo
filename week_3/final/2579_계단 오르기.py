import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N = int(input())
stairs = [0]
dp = [0] * (N + 1)

for i in range(N):
    stairs.append(int(input()))

# 첫 번째 계단부터 밟을 경우
if N >= 1:
    dp[1] = stairs[1]

if N >= 2:
    # 두 번째 계단은 첫 번째 계단 이후에 오르는 것이 최댓값
    dp[2] = dp[1] + stairs[2]

if N >= 3:
    # 세 번째 계단은 첫 번째 계단과 두 번째 계단 중 최댓값
    dp[3] = max(dp[1] + stairs[3], stairs[2] + stairs[3])

for i in range(4, N + 1):
    # i 번째 계단은 (i-2번 째 계단에서 2칸 점프했을 때, i-3번 째 계단과 i-1번 째 계단을 밟고 올라왔을 때의 값)
    dp[i] = max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i - 1] + stairs[i])

print(dp[N])
