import sys
import math

input = sys.stdin.readline

M, N, L = list(map(int, input().strip().split()))

animals = []

# 발사대
fire = list(map(int, input().split()))
    

fire.sort()

def binarySearch(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return right

count = 0
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    
    idx = binarySearch(fire, x)

    dist = abs(x - fire[idx]) + y
    dist_right = abs(x - fire[idx+1]) + y if idx < M-1 else float('inf')

    dist = min(dist, dist_right)

    if dist <= L:
        count += 1
print(count)

##################################################################################

# # 동물
# for _ in range(N):
#     animal = list(map(int, input().split()))
#     animals.append(animal)

# fire = sorted(fire)

# cnt = 0

# for x, y in animals:
#     start = x + y - L
#     end = y - y + L
#     left, right = 0, M - 1

#     while start <= end:
#         mid = (start + end) // 2
#         if fire[mid] >= start and fire[mid] <= end:
#             cnt += 1
#             break
#         elif fire[mid] < end:
#             left = mid + 1
#         else:
#             right = mid - 1

# print(cnt)