import sys
input = sys.stdin.readline

N = int(input())

arr = []

for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a,b))

arr = sorted(arr)
start = arr[0][0]
end   = arr[0][1]

ans = 0

for elem in arr:
    if end > elem[1]:
        continue

    if start < elem[0]:
        start = elem[0]

    end = elem[1]
    ans += elem[1] - start
    start = elem[1]

print(ans)