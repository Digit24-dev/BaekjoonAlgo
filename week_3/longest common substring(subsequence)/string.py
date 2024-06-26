
import sys

# str1 = "ACAYKP"
# str2 = "CAPCAK"

str1 = input()
str2 = input()

def debug():
    for i in range(len(str1) + 1):
        for j in range(len(str2) + 1):
            print(lcs[i][j], end=' ')
        print()

lcs = [[0] * (len(str1) + 1) for _ in range(len(str2) + 1)]

for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        input()
        debug()
        if str1[i - 1] == str2[j - 1]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j - 1])

debug()

print(lcs[len(str1)][len(str2)])
