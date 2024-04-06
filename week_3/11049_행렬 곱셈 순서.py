import sys

input = sys.stdin.readline

'''
5x3 3x2 2x6

5 3 2 6
'''

def mulMatrix(a: tuple, b: tuple):
    return a[0] * a[1] * b[1], (a[0], b[1])

N = int(input())

matrixes = []

for i in range(N):
    r, c = map(int, input().split())
    matrixes.append((r,c))

print(matrixes)


for i in range(len(matrixes) - 1):
    ret = mulMatrix(matrixes[i], matrixes[i+1])
    