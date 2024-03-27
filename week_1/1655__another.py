import bisect

N = int(input())
arr = []

for _ in range(N):
    num = int(input())
    # 이진 탐색을 사용해 삽입 위치를 찾고 요소를 삽입한다.
    bisect.insort(arr, num)
    # 리스트의 중간값을 찾는다.
    if len(arr) % 2 == 0:
        print(arr[len(arr) // 2 - 1])
    else:
        print(arr[len(arr) // 2])
