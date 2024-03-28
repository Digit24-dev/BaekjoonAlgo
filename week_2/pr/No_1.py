import sys

input = sys.stdin.readline

N = int(input())
M = N
cnt = 0
new_number = 0

while True :
    print(new_number)
    if new_number == M :
        break
    if N < 10 :
        N *= 10

    a = N // 10
    b = N % (a*10)

    if b == 0 :
        b = 10
    c = a + b
    
    if c >= 10 :
        c -= 10
    if b > 0 :
        new_number = (b*10) + c
    else :
        new_number = c
    cnt += 1
    N = new_number

if N == 0 :
    cnt = 1

print (cnt)