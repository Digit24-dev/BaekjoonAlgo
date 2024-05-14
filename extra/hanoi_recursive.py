
def hanoi(n):
    if n == 0:
        return 0
    return 2 * hanoi(n - 1) + 1

print(hanoi(5))

'''
재귀 함수는 점화식이다
f(n) = n x f(n - 1)
'''