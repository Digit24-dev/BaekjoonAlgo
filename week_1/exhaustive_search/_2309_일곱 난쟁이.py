arr = []
ans = []

def dfs(depth, idx):
    if depth == 7:
        _sum = sum(ans)
        if _sum == 100:
            ans.sort()
            for i in ans:
                print(i)
            exit(0)
        else:
            return
    for i in range(depth, len(arr)):
        ans.append(arr[i])
        dfs(depth + 1, i + 1)
        ans.pop()

for i in range(9):
    temp = int(input())
    arr.append(temp)

dfs(0, 0)

