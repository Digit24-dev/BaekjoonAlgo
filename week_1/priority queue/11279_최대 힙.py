import sys
import heapq

heap = []

N = int(input())

while N > 0:
    N -= 1
    X = int(sys.stdin.readline())
    
    if X == 0:
        print(-heapq.heappop(heap) if len(heap) > 0 else 0)

    else:
        heapq.heappush(heap, -X)
    