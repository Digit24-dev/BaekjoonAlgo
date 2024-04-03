import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

arr = [[] for _ in range(n)]

for i in range(n):
    temp = int(input())
    arr[i] = [(temp * j) for j in range(1, k // temp + 1)]

arr.sort()

# print(arr)

'''
배열 정렬까지는 완료.
거꾸로 진입하면서 K와 대조,
1) K 보다 작을 경우 -> index 오른쪽
1-1) index 오른쪽으로 옮겼는데 K보다 작을 경우 -> 반복
1-2) index 오른쪽으로 옮겼는데 K보다  클  경우 -> 
2) K 보다 클 경우   -> index 현재 보다 작은 위치로 내려감
'''

'''
>>> 만들어진 DP 테이블에서 제일 값이 높은 것 부터 DFS/BFS 탐색!
DFS vs BFS ?
맵에서 여러 값을 더해가며 값을 비교하겠다면 DFS를 선택하는 것이 맞겠으나,
시간 제한이 1초로 되어 있어서 조금 어렵다.
계산해 보았을 때 최악의 경우의 탐색이 10ms 인 것으로 보아 DFS를 사용해도 큰 문제는 없겠으나 함수의 스택? 도 쓰면서 생각해보니 크게 상관 없겠다.
'''
