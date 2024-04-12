import sys
import heapq
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N = int(input())
# rooms = [[] for _ in range(N + 1)]
rooms = []

for i in range(N):
    # 강의 번호 / 시작 시간 / 종료 시간
    a, b, c = map(int, input().split())
    # rooms.append((c, b, a))
    heapq.heappush(rooms, ((c - b), b, c, a))

# 강의 끝나는 시간 기준 오름차순 정렬
# print(rooms)

# rooms = sorted(rooms, key= lambda x: (x[0] - x[1], x[2]))

ret = []

prev = 0
ans = 0
# for i in rooms:
while rooms:
    _, end, start, num = heapq.heappop(rooms)

    if start >= prev:
        prev = start
        ans += 1
        ret.append(num)

print(ans)
for i in ret:
    print(i)