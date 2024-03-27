from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

arr = [0] * N
max_value = 0

for i in range(N):
    temp = int(input())
    arr[i] = temp
    max_value = max(max_value, temp)

def radixSort(arr):
    digit = 1
    queue = deque(arr)
    buckets = [deque() for _ in range(10)]

    while max_value >= digit:
        while queue:
            num = queue.popleft()
            buckets[(num // digit) % 10].append(num)

        for bucket in buckets:
            while bucket:
                queue.append(bucket.popleft())
        
        digit *= 10

    return queue

print(radixSort(arr))
