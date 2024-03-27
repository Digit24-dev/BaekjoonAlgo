import sys
 푸 는 중 
input = sys.stdin.readline

# 100,000
N = int(input())

maxArr = [0] * N
minArr = [0] * N

for i in range(N):
    number = int(input())
    
    maxArr[i] = number
    minArr[i] = number

    maxArr[:i+1] = sorted(maxArr[:i+1], reverse=True)
    minArr[:i+1] = sorted(minArr[:i+1], reverse=False)

    midIdx = i // 2

    print(min(maxArr[midIdx], minArr[midIdx]))
