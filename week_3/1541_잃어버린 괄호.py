import sys
input = sys.stdin.readline

line = input().strip()

buf = ""
ops = []
numArr = []

for c in line:
    try:
        int(c)
        buf += c
    except:
        ops.append(c)
        numArr.append(int(buf))
        buf = ""

numArr.append(int(buf))

# print(len(numArr))
# print((numArr))
# print(len(ops))
# print((ops))

# 100 + 20 - 30 - 30 + 20

ans = numArr[0]
idx = 1
for opIdx in range(0, len(ops)):
    # print(ans)
    # input()
    if ops[opIdx] == '+':
        ans += numArr[idx]
    else:
        if opIdx + 1 < len(ops):
            if ops[opIdx + 1] == '-':
                ans -= numArr[idx]
            elif ops[opIdx + 1] == '+':
                ops[opIdx + 1] = '-'
                ans -= numArr[idx]
        else:
            ans -= numArr[idx]
    idx += 1

print(ans)