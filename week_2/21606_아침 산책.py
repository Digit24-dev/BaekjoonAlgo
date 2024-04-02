from collections import deque
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
answer = 0

visited = [False] * (N + 1)
place = [0] + list(map(int, input().strip()))
graph = [[] for _ in range(N + 1)]

# # 인접 행렬 방식 - 메모리 초과 / 인접 리스트, deque 방식 - 2, 5번 시간 초과
# graph = [[0] * (N + 1) for _ in range(N + 1)]
# for _ in range(N-1):
#     u, v = map(int, input().split())
#     graph[u][v] = 1
#     graph[v][u] = 1

# stack = deque()

# for i in range(1, N + 1):
#     if place[i] == 1:
#         stack.append((i, 1))
#         visited[i] = True

#         while stack:
#             start, callStackNum = stack.pop()

#             if callStackNum > 1 and place[start] == 1:
#                 answer += 1
#                 visited[start] = False
#                 continue
#             for i in range(1, N + 1):
#                 if graph[start][i] == 1 and not visited[i]:
#                     stack.append((i, callStackNum + 1))
#                     visited[i] = True

#             # for next_node in graph[start]:
#             #     if not visited[next_node]:
#             #         stack.append((next_node, callStackNum + 1))
#             #         visited[next_node] = True
            
        
#         visited = [False] * (N + 1)

# print(answer)


# 백트래킹 dfs 5번 시간 초과
graph = [[] for _ in range(N + 1)]
def dfs(start, callStackNum):
    global answer

    # 종료 조건 (실내일 경우 Deep 하지말고 리턴, 콜스택은 1 이상이어야 함.)
    if callStackNum > 1 and place[start] == 1:
        answer += 1
        return

    # 그래프 노드 검색 - 해당 부분이 실외인 경우
    for i in graph[start]:
        if visited[i] == False:
            visited[i] = True
            dfs(i, callStackNum + 1)
            visited[i] = False

# 모든 정점에서 가능한 경로를 탐색해 본다.
for i in range(1, N + 1):
    # 실내인 경우에만 탐색 시작
    if place[i] == 1:
        visited[i] = True
        dfs(i)
        visited[i] = False

print(answer)