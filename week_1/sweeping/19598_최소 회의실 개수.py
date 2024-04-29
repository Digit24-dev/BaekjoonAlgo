'''
서준이는 아빠로부터 N개의 회의를 모두 진행할 수 있는 최소 회의실 개수를 구하라는 미션을 받았다. 
각 회의는 시작 시간과 끝나는 시간이 주어지고 한 회의실에서 동시에 두 개 이상의 회의가 진행될 수 없다. 
단, 회의는 한번 시작되면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 
회의의 시작 시간은 끝나는 시간보다 항상 작다. N이 너무 커서 괴로워 하는 우리 서준이를 도와주자.
'''

# 우선순위 큐를 사용한 그리디.
'''
진행되고 있는 강의 중의 가장 먼저 시작한 강의의 끝나는 시간이랑  다음에 진행될 강의의 시작 시간만 비교

1. 강의 정보를 정렬
2. 강의 정보들을 하나씩 우선순위 큐 -> 끝나는 시간 기준
3. 우선순위 큐에 들어있는 가장 먼저 시작하는 정보와 새롭게 들어갈 정보의 시작시간을 비교
4. if 새롭게 들어갈 강의 정보의 시작이 크거나 같으면 우선순위 큐에서 pop
5. 새롭게 들어갈 강의 정보의 끝나는 시각을 우선순위 큐에 넣어줌.
'''

import sys
import heapq
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    s, e = map(int, input().split())
    arr.append((s, e))

answer = 0

arr = sorted(arr, key= lambda x: (x[0]))
arrIdx = 0

heap = []

heapq.heappush(heap, arr[arrIdx])

while heap:
    cur = heapq.heappop(heap)

    if cur[1] < arr[arrIdx][0]:
        pass
    else:
        arrIdx += 1
        if arrIdx >= N: break
        heapq.heappush(heap, cur)
        heapq.heappush(heap, arr[arrIdx])

    answer = max(answer, len(heap))

print(answer)



import sys, heapq
input = sys.stdin.readline

N = int(input())
schedules = sorted([list(map(int, input().split())) for _ in range(N)])
h = []
for start, end in schedules:
    if h and h[0] <= start:
        heapq.heappop(h)
    heapq.heappush(h, end)

print(len(h))
