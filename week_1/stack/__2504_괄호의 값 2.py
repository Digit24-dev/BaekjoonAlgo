import sys

input = sys.stdin.readline

st = []
score = 0

word = input()

tmpScore = 1

for i in range(len(word)):
    if word[i] == '(':
        st.append('(')
        tmpScore *= 2
    elif word[i] == '[':
        st.append('[')
        tmpScore *= 3
    elif word[i] == ')':
        if not st or st[-1] != '(':
            score = 0
            break
        if word[i-1] == '(':
            score += tmpScore
        st.pop()
        tmpScore //= 2
    elif word[i] == ']':
        if not st or st[-1] != '[':
            score = 0
            break
        if word[i-1] == '[':
            score += tmpScore
        st.pop()
        tmpScore //= 3


if st:
    score = 0

print(score)