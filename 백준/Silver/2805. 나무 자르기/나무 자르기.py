import sys

input = sys.stdin.readline

# 최상위 높이에서 부터 2배씩 감소
# M 보다 커졌을 경우 이전 값과 비교해서 가까운 순으로 탐색
# M < x < 2*M

N, M = list(map(int, input().split()))
trees = list(map(int, input().split()))
start, end = 1, max(trees)

# 탐색할 범위를 지정한다
# 탐색할 범위 변경하는데,
# 조건에 따라 계산한 값이 요구한 값보다 작을 경우
#   이분 탐색 범위를 mid 기준 위로 올리고
# 조건에 따라 계산한 값이 요구한 값보다 클 경우
#   이분 탐색 범위를 mid 기준 아래로 내린다.

# 이분 탐색은 결국에 계산할 mid의 값을 변경하는 것이 아니고
# 탐색할 범위를 반으로 줄여 나가는 것과 같다.

def getTotal(H):
    sum = 0
    for i in trees:
        if i - H > 0:
            sum += i - H
    return sum

while start <= end: # and input():
    mid = (start + end) // 2

    sum = getTotal(mid)

    if sum >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)
