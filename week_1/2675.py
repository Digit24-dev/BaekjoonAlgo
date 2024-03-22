import sys

T = int(sys.stdin.readline())

for i in range(0, T):
    [R, S] = sys.stdin.readline().split()
    # split()과 split(' ')의 차이 -> 
    # split()은 null 문자를 자동으로 분류하여 포함시키지 아니함.
    # split(' ')으로 문자열을 파싱하면 null 문자도 포함하여 배열에 넣음.
    for x in S:
        print(x * int(R), end='')

    print()

    for idx in range(0, len(S) - 1):
        for j in range(0, int(R)):
            print(S[idx], end='')
    print()