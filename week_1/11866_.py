import sys
from collections import deque

N, K = (sys.stdin.readline().strip().split())

N = int(N)
K = int(K)

arr = [i for i in range(1, N + 1)]
a = deque()

for i in arr:
    a.append(i)

print('<', end='')

while N > 0:
    N = N - 1
    for _ in range(K):
        ret = a.popleft()
        a.append(ret)
    a.pop()
    if N > 0:
        print(ret, ', ', end='')
    else:
        print(ret, end='')
    

print('>', end='')