import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
t = b

while b:
    d = b%10
    b = b//10

    print(a * d)

print(a * t)