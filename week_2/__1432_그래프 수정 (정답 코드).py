import sys
import heapq

input = sys.stdin.readline

n = int(input())
node = [[] for _ in range((n+1))]

indegree = [0] * (n + 1)
answer = [0] * (n + 1)

def topology_sort():
    q = []
    for i in range(1, n+1):
        if indegree[i] == 0:
            heapq.heappush(q, -i)
    
    N = n

    while q:
        now = -heapq.heappop(q)
        answer[now] = N

        for i in node[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(q, -i)

        # N += 1
        N -= 1

# 인접 행렬 -> 인접 리스트로 변경
for v in range(1, n + 1):
    temp = [0] + list(map(int, input().strip()))
    for i in range(1, n + 1):
        if temp[i] == 1:
            node[i].append(v)
            indegree[v] += 1

topology_sort()

if answer.count(0) > 1:
    print(-1)
else:
    print(*answer[1:])

'''

이 문제를 최대 힙으로 밖에 풀 수 없는 이유
문제의 조건 중에 'V2의 번호는 V1' 보다 커야한다는 조건이 있다.

최소 힙을 사용하여 1번 index 부터 시작하게 된다면, 위상 정렬의 특성상
진입 차수가 0인 것 부터 들어가기 때문에 V2 > V1 인 조건을 만족하지 못할 수도 있다.

따라서 최대 힙을 사용하여 거꾸로 인덱싱을 하게 된다면 조건을 만족하여 답을 구할 수 있다.

__1432 아이디어 그림 참고

'''