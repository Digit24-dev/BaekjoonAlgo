import sys

n = int(sys.stdin.readline())

def solve(a : list) -> list:
    sum = 0
    for i in a:
        sum += i
    return sum
