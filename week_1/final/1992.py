import sys

input = sys.stdin.readline

N = int(input())
# mmap = [[None] * N for _ in range(N)]

arr = [[None] * N for _ in range(N)]

for i in range(N):
    line = input()
    arr[i] = line

##### END INPUT #####

def debug(arr):
    print()
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()

# debug(arr)

ans = []
cnt = 0

def partition(di, dj, divide):
    global cnt
    color = arr[di][dj]
    flag = False
    # print(arr[di][dj], di, dj, divide)
    
    for i in range(di, di + divide):
        for j in range(dj, dj + divide):
            if arr[i][j] != color:
                flag = True
                break
            else:
                pass
    
    if flag:
        ans.append('(')
        partition(di            , dj            , divide//2)
        partition(di            , dj + divide//2, divide//2)
        partition(di + divide//2, dj            , divide//2)
        partition(di + divide//2, dj + divide//2, divide//2)
        ans.append(')')
    else:
        ans.append(color)

partition(0, 0, N)

# print(*ans)
for i in ans:
    print(i,end='')



#################################
######## 다른 방식의 코드 ########
#################################
result = 0
data = []

def one_color_check(x, y, size):
    global result    

    sum_value = 0
    for i in range(y, y + size):
        sum_value += sum(data[i][x : x + size])
    
    if sum_value == 0:
        result += '0'
    elif sum_value == size**2:
        result += '1'
    else:
        result += '('
        one_color_check(x, y, size//2)
        one_color_check(x + size//2, y, size//2)
        one_color_check(x, y + size//2, size//2)
        one_color_check(x + size//2, y + size//2, size//2)
        result += ')'

one_color_check(0, 0, N)
#################################
########        END      ########
#################################