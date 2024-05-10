import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    line = input()
    st = []
    flag = False
    for c in line:
        if c == '(':
            st.append(c)
        elif c == ')':
            if not st:
                print("NO")
                flag = True
                break
            else:
                st.pop()
    if flag:
        pass
    elif st:
        print("NO")
    else:
        print("YES")