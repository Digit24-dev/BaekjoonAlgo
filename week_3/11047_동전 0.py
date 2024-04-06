import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [0] * (N)

for i in range(N):
    arr[i] = int(input())

ans = 0
for i in range(N-1, -1, -1):
    if K // arr[i] >= 1:
        ans += K // arr[i]
        K = K % arr[i]

print(ans)