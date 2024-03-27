### 다시 풀어 보기 ###
import sys

input = sys.stdin.readline

st = []
score = 0

word = input()

isWrong = False

tmp = 1

for i in range(len(word)):
    if word[i] == '(':
        st.append('(')
        tmp *= 2
    elif word[i] == '[':
        st.append('[')
        tmp *= 3
    elif word[i] == ')':
        if not st or st[-1] != '(':
            score = 0
            break
        if word[i-1] == '(':
            score += tmp
        st.pop()
        tmp //= 2
    elif word[i] == ']':
        if not st or st[-1] != '[':
            score = 0
            break
        if word[i-1] == '[':
            score += tmp
        st.pop()
        tmp //= 3

if st:
    score = 0

print(score)
