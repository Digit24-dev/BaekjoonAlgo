import time
import sys

T = int(sys.stdin.readline())

start = time.time()

arr = [0 for i in range(10001)]
arr[1] = 0

for i in range(2, 10000):
    for j in range(2, 10000):
        if i * j >= 10001:
            break
        arr[i * j] = 1

end = time.time()

for _ in range(0, T):
    N = int(sys.stdin.readline())
    
    for i in range(2, int(N/2) + 1):
        if arr[i] != 0:
            continue
        if arr[N - i] == 0:
            a = i
            b = N - i
        
    print(a, b)

print(f"{end - start: .5f} sec")