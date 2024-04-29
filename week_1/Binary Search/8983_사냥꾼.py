import sys
import math

input = sys.stdin.readline

M, N, L = list(map(int, input().strip().split()))

# 사대의 위치
camp = list(map(int, input().split()))

animals = [(0, 0) for _ in range(N)]

# 동물의 위치
for i in range(N):
    x, y = map(int, input().split())
    animals[i] = (x, y)

mid = camp[len(camp) // 2]

print(mid)
print(camp)
print(animals)

camp = sorted(camp)
animals = sorted(animals, key= lambda x: (abs(mid - x[0]) + x[1]))

print(camp)
print(animals)