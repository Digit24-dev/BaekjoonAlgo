import time
import sys
input = sys.stdin.readline

# N, r, c = map(int, input().split())

# base = ((r-1) >> 1 << 1) * 2**(N)
# graph = [[i + j for i in range(2**N)] for j in range(2**N)]

# cnt = 0

# def div(i, j, div):
#     if div == 1:
#         return 
#     if i == r - 1 and j == c - 1:
#         print(cnt)
#         return

#     div(i,          j         ,   div//2)
#     div(i,          j + div//2,   div//2)
#     div(i + div//2, j         ,   div//2)
#     div(i + div//2, j + div//2,   div//2)

# for i in range(2**N):
#     for j in range(2**N):
#         print(graph[i][j], end=' ')
#     print()
# # ............................................................ #

N, r, c = map(int, input().split())

def sol(N, r, c):
    if N == 0:
        return 0
    
    return 2*(r % 2) + (c % 2) + 4 * sol(N-1, int(r/2), int(c/2))

print(sol(N, r, c))