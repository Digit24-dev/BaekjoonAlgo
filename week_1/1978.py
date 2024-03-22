import sys

N = int(sys.stdin.readline())

arr = [0 for i in range(1001)]
arr[1] = 1

for i in range(2, 1001):
    for j in range(2, 1001):
        if i * j >= 1001:
            break
        arr[i * j] = 1

line = sys.stdin.readline().split()

for _ in range(0, N):    
    cnt = 0

    for idx in line:
        if arr[int(idx)] == 0:
            cnt = cnt + 1

print(cnt)
