from typing import MutableSequence

def qsort(a: MutableSequence, l: int, r:int):

    pl = l
    pr = r
    mid = a[(l+r) // 2]

    while pl <= pr:
        while a[pl] < mid : pl += 1
        while a[pr] > mid : pr -= 1
        
        print('포인터 먼저 이동 결과 => ', end='')
        print('pl =', pl, ', pr = ', pr)

        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
        
        print('if문 이후 => ', end='')
        print('pl = ', pl, ', pr = ', pr)

        if l < pr : qsort(a, l, pr)
        if pl < r : qsort(a, pl, r)

N = int(input())
arr = []

for _ in range(N):
    a = int(input())
    arr.append(a)

qsort(arr, 0, len(arr) - 1)