import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

INF = 10001
dp = [INF] * (N + 1)
check = [[] for _ in range(N + 1)]
aa = set()

for _ in range(M):
    a = int(input())
    aa.add(a)

# print(dp)
# bfs 탐색을 진행하면서 dp 채우기..
def bfs(p_idx, p_count, p_jmp):
    q = deque()
    q.append((p_idx, p_count, p_jmp))

    while q:
        idx, count, jmp = q.popleft()
        
        dp[idx] = min(dp[idx], count)

        for i in [1, 0, -1]:
            if jmp + i > 0:
                next = idx + i + jmp
                if next == N:
                    return count + 1
                if 1 < next < N and next not in aa and jmp + i not in check[next]:
                    check.append(jmp + i)
                    q.append((next, count + 1, jmp + i))

    return -1

print(bfs(1, 0, 0))