import sys

input = sys.stdin.readline

K = int(input())
st = []

for _ in range(K):
    t = int(input())
    if t == 0:
        st.pop()
    else:
        st.append(t)

ans = 0
for elem in st:
    ans += elem

print(ans)