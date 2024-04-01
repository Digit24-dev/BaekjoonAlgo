import sys
input = sys.stdin.readline

def get(current_index, sum):
    global count
    # 종료조건 : 인덱스를 넘어갔을 때
    if current_index >= n:
        return 0
    
    # 먼저 현재의 인덱스 값을 더해주고 나중에 
    # 인덱스 값을 포함하지 않을 경우에 빼서 재귀
    sum += arr[current_index]
    if sum == s:
        count += 1

    # 현 인덱스 값을 포함하는 경우
    get(current_index + 1, sum)
    # 현 인덱스 값을 포함하지 않는 경우
    get(current_index + 1, sum - arr[current_index])

if __name__ == "__main__":
    n, s = map(int, input().rstrip().split())
    arr = list(map(int, input().rstrip().split(" ")))

    count = 0
    get(0, 0)

    print(count)
    