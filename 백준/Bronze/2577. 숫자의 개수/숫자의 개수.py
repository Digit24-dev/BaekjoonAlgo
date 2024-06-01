A = int(input())
B = int(input())
C = int(input())

sum = str(A * B * C)

numArr = [0] * 10
for c in sum:
    numArr[int(c)] += 1

for i in numArr:
    print(i)