import sys
import heapq
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N = int(input())
rooms = []

for i in range(N):
    # 강의 번호 / 시작 시간 / 종료 시간
    a, b, c = map(int, input().split())
    # rooms.append((c, b, a))
    heapq.heappush(rooms, ((c - b), b, c, a))

