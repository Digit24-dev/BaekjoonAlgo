import heapq
import sys

input = sys.stdin.readline

##### INPUT #####

N = int(input())

maps = []
for _ in range(N):
    i, j = list(map(int, input().split()))
    maps.append([i,j])
    
d = int(input())

### END INPUT ###

maps = sorted(maps, key = lambda x: (x[0] ,x[1]))

print(maps)