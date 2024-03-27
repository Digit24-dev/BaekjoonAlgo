import sys

input = sys.stdin.readline

st = []
score = 0

line = input()
a = list(line)
b = []

isWrong = False

for c in a:
    n = len(a)
    # input()

    if c == '(':
        st.append(c)

    elif c == '[':
        st.append(c)

    elif c == ')':
        ff = st.pop()
        
        # 틀린 괄호
        if ff != '(':
            isWrong = True
            break

        else:
            # 올바른 괄호
            if (st[len(st) - 1] == '[' or st[len(st) - 1] == '('):
            # if len(st) == 0:
                sss = b.pop()
                sss*=2
                b.append(sss)
            elif len(st) != 0:
                b.append(2)

    elif c == ']':
        ff = st.pop()

        # 틀린 괄호
        if ff != '[':
            isWrong = True
            break

        else:
            # 올바른 괄호
            if (st[len(st) - 1] == '[' or st[len(st) - 1] == '('):
            # if len(st) == 0:
                sss = b.pop()
                sss *= 3
                b.append(sss)
            elif len(st) != 0:
                b.append(3)

score = sum(b)

if isWrong:
    score = 0

print(score)
