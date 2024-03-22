import sys

N = int(sys.stdin.readline())

a = []
s = set()

# input
for _ in range(0, N):
    str = sys.stdin.readline().strip()

    s.add(str)

a = list(s)

# solution
a.sort(key=lambda x:(len(x), x))

for c in a:
    print(c)

