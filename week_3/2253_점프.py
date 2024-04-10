import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(15000)

N, M = map(int, input().split())

INF = 10001
dp = [INF] * (N + 1)
visited = [False] * (N + 1)

for _ in range(M):
    a = int(input())
    dp[a] = -1

dp[0] = 0
dp[1] = 1

# print(dp)
# bfs 탐색을 진행하면서 dp 채우기..
def bfs(p_idx, p_count, p_jmp):
    q = deque()
    q.append((p_idx, p_count, p_jmp))
    visited[p_idx] = True

    while q:
        idx, count, jmp = q.popleft()
        # cur = q.popleft()
        
        dp[idx] = min(dp[idx], count)
        
        if idx == N:
            q.clear()
            break

        for i in [1, 0, -1]:
            if 1 < (idx + jmp + i) <= N and not visited[idx + jmp + i] and dp[(idx + jmp + i)] != -1:
                visited[idx + jmp + i] = True
                q.append((idx + jmp + i, count + 1, jmp + i))
    
# bfs(1, 1, 1)

# dfs 탐색을 진행하면서 dp 채우기..
def dfs(idx, count, jmp):
    visited[idx] = True
    # if dp[idx] == -1:
    #     # 점프할 수 없는 돌
    #     return
    
    # if idx >= N or idx < 1:
    #     # 목표에 도달했을 경우 혹은 1보다 작은 쪽으로 갈 경우
    #     return
    
    dp[idx] = min(dp[idx], count)

    for var in [1, 0, -1]:
        if (idx + jmp + var) <= N and dp[idx + jmp + var] == INF and dp[idx + jmp + var] != -1: # <= (?)
            dfs(idx + jmp + var, count + 1, jmp + var)

    # dfs(idx + jmp - 1, count + 1, jmp - 1)
    # dfs(idx + jmp    , count + 1, jmp)
    # dfs(idx + jmp + 1, count + 1, jmp + 1)

dfs(1, 1, 1)

print(dp)
if dp[N] != INF:
    print(dp[N])
else:
    print(-1)