T = int(input())


def check(strings):
    stack = []

    for i in strings:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                print("NO")
                return
            else:
                stack.pop()

    if not stack:
        print("YES")
        return
    else:
        print("NO")
        return


for _ in range(T):
    n = input()
    check(n)


