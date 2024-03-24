import sys
from heapq import heapify, heappop, heappush

a = []

# 100,000
N = int(input())

while N > 0:
    N -= 1
    a.append(int(sys.stdin.readline()))
    heapify(a)

    print(a[len(a)//2])
