import sys
import heapq

input = sys.stdin.readline

heap = []
arr = []
ans = 0
n = int(input())
for _ in range(n):
    s, e = map(int, input().split())

    arr.append((s, e))

d = int(input())

# 시작 시간 기준으로 정렬
arr = sorted(arr, key= lambda x: (x[0]))
idx = 0

