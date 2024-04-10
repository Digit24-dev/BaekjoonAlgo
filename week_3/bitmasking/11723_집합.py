import sys
input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
    command = input().split()
    if command == "empty":
        S = set()
    elif command == "all":
        