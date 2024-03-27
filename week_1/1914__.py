import sys

def hanoi(n, s, t):
    if n == 1:
        print(s, t)
        return
    
    hanoi(n-1, s, 6 - s - t)
    print(s, t)
    hanoi(n-1, 6 - s - t, t)

N = int(sys.stdin.readline())
print(2**N - 1)

if N <= 20:
    hanoi(N, 1, 3)
