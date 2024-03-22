import sys

N, K = (sys.stdin.readline().strip().split())

N = int(N)
K = int(K)

arr = [i for i in range(1, N + 1)]

idx = K + 1

print('<', end='')

while N > 0:
    if arr[idx] == -1: continue
    print(arr[idx], end='')
    arr[idx] = -1
    idx = (idx + K - 1) % N
    print(', ', end='')
    N = N - 1

print('>', end='')