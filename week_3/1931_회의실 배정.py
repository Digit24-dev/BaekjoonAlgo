import sys
input = sys.stdin.readline

N = int(input())

arr2 = []

for i in range(N):
    start, end = map(int, input().split())
    arr2.append((start,end))

# x[1] 으로 정렬한 후에 x[0]으로 정렬하기
arr2 = sorted(arr2, key= lambda x: (x[1], x[0]))

prev = 0
ans = 0
for start, end in arr2:
    if start >= prev:
        ans += 1
        prev = end

print(ans)