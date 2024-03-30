import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수(n)과 간선의 개수(m) 입력
n = int(input())
m = int(input())

# 2차원 리스트(그래프)를 만들고, 무한대로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A -> B로 가는 비용을 C라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드-워셜 알고리즘 수행
# 중간 지점 K를 변경해 나가면서 점화식의 개선을 구해 나간다.
    
print('==== 플로이드 와샬 진행중 ====')

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == 4 and b == 2:
                print(k, graph[a][b], ' -> ', graph[a][k], graph[k][b])
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 만약 네 개의 간선을 통해 가는 경로일 경우에 생각을 해보면
# a->b 가는 경로는 없을 때 어떻게 아는가?
# a < k < b 일 경우
# a->k 까지 가는 경로는 이전 dp를 통하여 구현 되었을 것이고
# k->b 또한 구해질 것이므로
# a -> b 까지 가는 경로는 k 와 a, b가 반복문을 돎에 따라 자동으로 채워질 것이다!

print('==== here is your result ! ====')

# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print('INFINITY', end=' ')
        else:
            print(graph[a][b], end=' ')
    print()

# sample input
# 4
# 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2