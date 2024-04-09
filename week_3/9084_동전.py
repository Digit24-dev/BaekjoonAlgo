import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    M = int(input())
    
    dp = [[0] * (M + 1) for _ in range(len(arr) + 1)]
    
    for i in range(len(arr) + 1):
        dp[i][0] = 1

    for i in range(len(arr)):
        for j in range(1, M + 1):
            if (j - arr[i]) >= 0:
                dp[i + 1][j] = dp[i + 1][j - arr[i]] + dp[i][j]
            else:
                dp[i + 1][j] = dp[i][j]

    print(dp[len(arr)][M])


'''

/   0   1   2   3   4   5   6   7   8   9   10  ...      1000
--------------------------------------------------------------
0   0   0   0   0   0   0   0   0   0   0   0   ...        0
1   0   1   1   1   1   1   1   1   1   1   1   1          1
2   0   0   1   0   1   0   1   0   1   0   1   ...        1
12  0   0   

/   0   1   2   3   4   5   6   7   8   9   10  ...      100
-------------------------------------------------------------
0   0   0   0   0   0   0   0   0   0   0   0   ...        0
1   0   1   1   1   1   1   1   1   1   1   1   1          1
5   0   1   1   1   1   2   2   2   2   2   3   ...        21
10  0   1   1   1   1   2   2   2   2   2   4   ...        

/   20  25
1   1   1
5   5   "5를 뺀 20을 만드는 경우 + 15를 만드는 경우 + 10을 만드는 경우
10  8   

dp[i][j] = max(dp[i-1][j//i] + dp[i-1][j%i], dp[i-1][j])

'''

