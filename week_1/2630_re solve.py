N = 0
map = [[0] * 128 for _ in range(128)]
ans = [0, 0]

def minput():
    global N
    N = int(input())
    for i in range(N):
        temp = input().split()
        for j in range(N):
            map[i][j] = int(temp[j])

def partition(lui, luj, divide):
    curColor = map[lui][luj]
    ret = 0
    for i in range(lui, lui + divide):
        for j in range(luj, luj + divide):
            if map[i][j] == curColor:
                pass
            else:
                ret = 1
                break
    
    if ret == 0:
        ans[curColor] += 1
    else:
        partition(lui, luj, divide // 2)
        partition(lui + divide // 2, luj, divide // 2)
        partition(lui, luj + divide // 2, divide // 2)
        partition(lui + divide // 2, luj + divide // 2, divide // 2)

def solution():
    partition(0, 0, N)

minput()
solution()
print(ans[0])
print(ans[1])

