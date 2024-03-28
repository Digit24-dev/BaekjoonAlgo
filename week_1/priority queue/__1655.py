import sys
import heapq

input = sys.stdin.readline

N = int(input())
left = []
right = []

for _ in range(N):
    num = int(input())

    if len(left) == len(right):
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)

    if right and right[0] < -left[0]:
        leftValue = heapq.heappop(left)
        rightValue = heapq.heappop(right)

        heapq.heappush(left, rightValue)
        heapq.heappush(right, leftValue)

    print(-left[0])
