import sys
input = sys.stdin.readline

dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
    # 메모이제이션을 활용하여 값을 채워 넣음
for a in range(21):
    for b in range(21):
        for c in range(21):
            if a == 0 or b == 0 or c == 0:
                dp[a][b][c] = 1
            elif a < b < c:
                dp[a][b][c] = dp[a][b][c-1] + dp[a][b-1][c-1] - dp[a][b-1][c]
            else:
                dp[a][b][c] = dp[a-1][b][c] + dp[a-1][b-1][c] + dp[a-1][b][c-1] - dp[a-1][b-1][c-1]

    '''
    if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
        1

    if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
        w(20, 20, 20)

    if a < b and b < c, then w(a, b, c) returns:
        w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

    otherwise it returns:
        w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    '''
    # 특정 a, b, c 값에 대해 계산된 결과를 반환하는 함수
def get_value(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return dp[20][20][20]
    return dp[a][b][c]
    

while True:
    a, b, c = map(int, input().split())

    if a == -1 and b == -1 and c == -1:
        break

    print('w(', a, ', ', b, ', ', c, ') = ', end='', sep='')
    print(get_value(a, b, c))