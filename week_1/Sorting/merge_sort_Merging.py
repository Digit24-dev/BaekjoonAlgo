from typing import Sequence, MutableSequence

# 병합하는 함수
def merge_sorted_list(a: Sequence, b:Sequence, c:MutableSequence) -> None:
    pa, pb, pc = 0, 0, 0

    # merge() 함수는 원소의 수가 na인 배열 a와 nb인 배열 b를 병합하여 c에 저장한다.

    na , nb, nc = len(a), len(b), len(c)
    
    while pa < na and pb < nb:
        if a[pa] <= b[pb]:
            c[pc] = a[pa]
            pa += 1
        else:
            c[pc] = b[pb]
            pb += 1
        pc += 1

    while pa < na:
        c[pc] = a[pa]
        pa += 1
        pc += 1

    while pb < na:
        c[pc] = b[pb]
        pb += 1
        pc += 1

# ==> c = list(heapq.merge(a, b))
        
    
