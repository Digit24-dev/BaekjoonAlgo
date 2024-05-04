import sys
input = sys.stdin.readline

N, X = map(int, input().split())

A = list(map(int, input().split()))

for elem in A:
    if elem < X:
        print(elem, end=' ')
print()
