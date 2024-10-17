import sys
input = sys.stdin.readline

L, C = map(int, input().split())
arr = input().split()

arr = sorted(arr)
# print(arr)

def dfs(idx, a, b, bucket: list):
    # print(bucket)
    bucket.append(arr[idx])
    if arr[idx] == 'a' or arr[idx] == 'e' or arr[idx] == 'i' or arr[idx] == 'o' or arr[idx] == 'u' :
        a += 1
    else :
        b += 1
    
    if len(bucket) == L and a >= 1 and b >= 2:
        for a in bucket:
            print(a, end='')
        print()
        return
    
    for i in range(idx + 1, C):
        dfs(i, a, b, bucket)
        bucket.pop(-1)

for i in range(0, C-L+1):
    buck = []
    dfs(i, 0, 0, buck)