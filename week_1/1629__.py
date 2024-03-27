import sys

A,B,C = map(int, sys.stdin.readline().strip().split())

def pwr(A, n):
    if n == 1:
        return A % C
    else:
        tmp = pwr(A, n//2)
        if n & 0x01 == 0:
            return (tmp * tmp) % C
        else:
            return (tmp * tmp * A) % C
        
print(pwr(A, B))