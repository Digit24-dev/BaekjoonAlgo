import sys
from collections import deque
input = sys.stdin.readline

def cnt_if_splited(want_array):
    # 얼마나 시간이 지났는가?
    time_cnt = 0
    
    di_x = [0,0,1,-1]
    di_y = [1,-1,0,0]
    while True:
        # 몇개로 나뉘었는가?
        split_cnt = 0
        visited_array = [[0] * M for _ in range(N)]
        # 그 다음 array로 사용할 것
        next_array = [[0] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                # 0인 곳은 방문표시 그냥 해놓음
                if not want_array[i][j]:
                    visited_array[i][j] = 1
                # 섬 밟으면 그 섬 다 BFS로 탐색함
                if want_array[i][j] and not visited_array[i][j]:
                    visited_array[i][j] = 1
                    split_cnt += 1
                    stack = deque()
                    stack.append([i, j])
                    while stack:
                        x, y = stack.popleft()
                        # 해당 지점에서 0을 맞닿은 곳의 개수를 카운트할 것임
                        zero_cnt = 0
                        for di in range(4):
                            new_x = x + di_x[di]
                            new_y = y + di_y[di]
                            # 섬의 다른 지점은 방문표시하고 스택에 넣기
                            if want_array[new_x][new_y] and not visited_array[new_x][new_y]:
                                visited_array[new_x][new_y] = 1
                                stack.append([new_x, new_y])
                            # 0인 곳은 zero_cnt에 추가
                            elif not want_array[new_x][new_y]:
                                zero_cnt += 1
                        # 다음 array로 사용할 곳에 1초 후 녹은 크기를 넣어줌, 0미만은 0으로 
                        next_array[x][y] = want_array[x][y] - zero_cnt
                        if next_array[x][y] < 0:
                            next_array[x][y] = 0
        # 다음 반복시 사용할 array 바꿔주기
        want_array = next_array
        # 시간 지났으니 + 1초
        time_cnt += 1
        # 아예 섬이 없었으면 0
        if split_cnt == 0:
            return 0
        # 2 이상으로 나눠졌으면 이전 시간대에 나눠졌다는 뜻이니 -1 해줌
        if split_cnt >= 2:
            return time_cnt - 1


N, M = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
result = cnt_if_splited(array)
print(result)
