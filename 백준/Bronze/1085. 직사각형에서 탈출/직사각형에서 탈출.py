
x, y, w, h = map(int, input().split())

ans = int(1e9)

ans = min(ans, x)
ans = min(ans, abs(x - w))
ans = min(ans, y)
ans = min(ans, abs(y - h))

print(ans)
