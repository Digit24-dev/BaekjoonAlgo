import sys
import heapq

input = sys.stdin.readline

N = int(input())
left = []
right = []

for _ in range(N):
    num = int(input())

    # 최대 최소 힙에 번갈아 가면서 데이터를 넣는다.
    # (최대 힙에 먼저 데이터를 넣는다.)
    
    if len(left) == len(right):
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)

    # 최소 힙에 데이터가 있고,
    # 최소 힙의 루트 노드가 최대 힙의 루트 노드 보다
    # 작을 경우
        
    if right and right[0] < -left[0]:   
        # 오른쪽 힙에는 최소 힙을 구현했으므로
        # 왼쪽 힙은 최대 힙, 오른쪽 힙이 최소 힙이면 가운데 값은 중간 값을 갖는다.
        
        # 최대 값과 최소 값을 추출
        leftVal = heapq.heappop(left)
        rightVal = heapq.heappop(right)

        # 두 값을 교차하여 서로의 힙에 저장
        heapq.heappush(left, -rightVal)
        heapq.heappush(right, -leftVal)

    print(-left[0])