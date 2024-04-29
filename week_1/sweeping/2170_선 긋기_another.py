import sys

INF = sys.maxsize

n = int(sys.stdin.readline())

data = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
data.sort()

start = -INF
end = -INF
length = 0

for left, right in data:
    if end < left:
        length += end - start
        start = left
    if end < right:
        end = right

length += end - start
print(length)
