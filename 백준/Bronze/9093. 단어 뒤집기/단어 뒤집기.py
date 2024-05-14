import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    arr = list(input().split())
    
    for str in arr:
        for i in range(len(str) - 1, -1, -1):
            print(str[i], end='')
        print(end=' ')
    print()

