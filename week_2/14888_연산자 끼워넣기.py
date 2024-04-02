import math
import sys
from collections import deque
input = sys.stdin.readline

INF = int(1e10)

N = int(input())
arr = list(map(int, input().split()))
adds, subs, muls, divs = map(int, input().split())
stackedOperators = [adds, subs, muls, divs]

maxAnswer = -INF
minAnswer =  INF

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a < 0:
        return -(abs(a) // b)
    else:
        return a // b

command_dic = {
    0: add,
    1: sub,
    2: mul,
    3: div
}

def dfs(arrIndex, command, data):
    global minAnswer, maxAnswer

    # 종료 조건
    if arrIndex == N - 2:
        # print('## DEBUG: ', arrIndex, command, data)
        data = command_dic[command](data, arr[arrIndex + 1])
        # print('## DEBUG: ', data)

        minAnswer = min(minAnswer, data)
        maxAnswer = max(maxAnswer, data)
        return
    
    # 로직
    # print('DEBUG: ', arrIndex, command, data)
    d = command_dic[command](data, arr[arrIndex + 1])
    # print('DEBUG: ', arrIndex, command, d)

    # 탐색
    for i in range(4):
        if stackedOperators[i] > 0:
            stackedOperators[i] -= 1
            dfs(arrIndex + 1, i, d)
            stackedOperators[i] += 1


for i in range(4):
    if stackedOperators[i] > 0:
        stackedOperators[i] -= 1
        dfs(0, i, arr[0])
        stackedOperators[i] += 1

print(maxAnswer)
print(minAnswer)