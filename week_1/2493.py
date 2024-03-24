import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))

st = []
ans = [0 for _ in range(N)]

for i in range(len(arr)-1, -1, -1):
    if len(st) == 0:
        st.append((arr[i], i))
    elif st[len(st) - 1][0] <= arr[i]:
        while len(st) > 0 and st[len(st) - 1][0] <= arr[i]:
            a = st.pop()
            ans[a[1]] = i + 1
        st.append((arr[i], i))
    else:
        st.append((arr[i], i))

print(*ans)

# def find_receiver_towers(tower_heights):
#     n = len(tower_heights)
#     receivers = [0] * n  # 각 탑이 수신하는 탑을 저장할 리스트
#     stack = []  # 레이저 신호를 발사한 탑을 저장할 스택

#     for i in range(n):
#         # 스택이 비어있지 않고, 현재 탑의 높이가 스택의 탑보다 높거나 같은 경우
#         while stack and tower_heights[stack[-1]] <= tower_heights[i]:
#             stack.pop()  # 스택의 탑은 현재 탑에 의해 가려짐
#         if stack:
#             receivers[i] = stack[-1] + 1  # 현재 탑의 수신 탑을 스택의 탑으로 설정
#         stack.append(i)  # 현재 탑을 스택에 추가

#     return receivers

# # 입력 받기
# n = int(input())
# tower_heights = list(map(int, input().split()))

# # 결과 출력
# result = find_receiver_towers(tower_heights)
# print(*result)
