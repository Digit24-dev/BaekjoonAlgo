import sys

input = sys.stdin.readline

def printMatrix(arr):
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()

N, B = map(int, input().split())

arr = [[0] * N for _ in range(N)]

# input #
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        arr[i][j] = line[j]

def MultiplyMatrix(arr, brr):
    crr = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            sum = 0
            for k in range(N):
                sum += (arr[i][k] * brr[k][j])

            crr[i][j] = sum % 1000

    return crr

def DivideC(array):
    for i in range(N):
        for j in range(N):
            array[i][j] %= 1000
    return array

# divide and conquer
def DivideAndConquer(array, pwr):
    if pwr == 1:
        return DivideC(array)
    else:
        tmp = DivideAndConquer(array, pwr//2)
        
        if pwr & 0x01:
            # 홀수
            return MultiplyMatrix(MultiplyMatrix(tmp, tmp), array)
        else:
            # 짝수
            return MultiplyMatrix(tmp, tmp)
        
ret = DivideAndConquer(arr, B)
printMatrix(ret)

# ret = arr
# cnt = 1
# print('초기 행렬')
# print(ret)
# while input():
#     ret = MultiplyMatrix(ret, arr)
#     print(cnt, ' pwr')
#     print(ret)
#     cnt += 1