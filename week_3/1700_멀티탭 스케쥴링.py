import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

### first try
# i = N
# ans = 0 # 바뀐 데이터 개수

# prevTap = arr[0 : N]
# # print(prevTap)

# while i <= len(arr):
#     # 이전이랑 비교해서 현재 데이터 저장
#     window = arr[i : i + N]
#     cnt = 0

#     for item in window:
#         if item in prevTap:
#             pass
#         else:
#             ans += 1

#     prevTap = arr[i : i + N]
#     # print(prevTap)
#     i += N

# print(ans)

plug = set()
cnt = 0

def find_latest(idx):
    result = 0
    max_idx = -1
    for num in plug:
        try:
            num_idx = arr[idx:].index(num)
        except:
            num_idx = K
        if max_idx < num_idx:
            result, max_idx = num, num_idx

    return result

for idx, num in enumerate(arr):
    plug.add(num)
    # 
    if len(plug) > N:
        cnt += 1
        latest_used = find_latest(idx)
        plug.discard(latest_used)

print(cnt)