from typing import MutableSequence

def quick_sort_recursive(arr : MutableSequence) -> None:
    qsort(arr, 0, len(arr) - 1)

def qsort(a: MutableSequence, l: int, r:int):

    pl = l
    pr = r
    mid = a[(l+r) // 2]

    while pl <= pr:
        while a[pl] < mid : pl += 1
        while a[pr] > mid : pr -= 1

        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
        # 여기까지 진행시 mid, pl, pr 위치의 값 고정하여 분할.
        
        '''
        # 그렇게 된다면 원래 정렬하고자 한 구간은 [l ~ r]
        
        # 위 분할에서 pl과 pr이 맞 교환 됐으므로
        ### 1) a[pl]과 a[pr]이 mid와 일치할 경우: while문의 비교문에 '='이 없기 때문에 빗겨간다.
        ### 2) 일치하지 않을 경우 : if 문에 의해 걸침
        # 분할된 구간은 [l ~ pr] [pl ~ r]
        # 분할된 구간 각 qsort 재귀 호출
        '''
        
        if l < pr : qsort(a, l, pr)
        if pl < r : qsort(a, pl, r)
    


N = int(input())
arr = []
while N > 0:
    N -= 1
    arr.append(int(input()))

quick_sort_recursive(arr)

for i in arr:
    print(i)