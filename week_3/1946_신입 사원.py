import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    arr = [()] * (N)
    toTerminate = []

    for i in range(N):
        paper, interview = map(int, input().split())
        arr[i] = (paper, interview)

    arr = sorted(arr)
    least = arr[0][1]

    for i in range(N):
        if arr[i][1] > least:
            toTerminate.append(i)
            continue
        least = min(least, arr[i][1])

    print(len(arr) - len(toTerminate))
