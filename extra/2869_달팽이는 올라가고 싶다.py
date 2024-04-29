import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())

if V <= A:
    print(1)
    exit(0)

if (V - A) < (A - B):
    ret = 1
else:
    if (V - A) % (A - B) > 0:
        ret = (V - A) // (A - B) + 1
    else:
        ret = (V - A) // (A - B)

print(ret + 1)