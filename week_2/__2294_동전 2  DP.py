import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

li = []

for i in range(n):
    li.append(int(input().rstrip()))

dp = [10001] * (k + 1)
dp[0] = 0

for num in li:
    for i in range(num, k+1):
        ### dp[i - num] + 1 -> num 현재 선택한 동전 i - num 의 dp 값 선택하고
        ### - num 을 했으므로 동전 갯수 + 1
        dp[i] = min(dp[i], dp[i - num] + 1)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])

'''
DP의 index를 구하고자 하는 값으로 대입하여 푼다.
'''
