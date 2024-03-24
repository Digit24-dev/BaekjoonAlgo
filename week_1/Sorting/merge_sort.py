from typing import Sequence, MutableSequence

# MERGE SORT !

def merge_sort(a : MutableSequence) -> None:
    
    def _merge_sort(a :MutableSequence, l :int, r :int) -> None:
    
        if l < r:
            mid = (l + r) // 2

            _merge_sort(a, l, mid)
            _merge_sort(a, mid + 1, r)
        
            p = j = 0
            i = k = l

            while i <= mid:
                buff[p] = a[i]
                p += 1
                i += 1

            while i <= r and j < p:
                if buff[j] <= a[i]:
                    a[k] = buff[j]
                    j += 1
                else:
                    a[k] = a[i]
                    i += 1
                k += 1

            while j < p:
                a[k] = buff[j]
                k += 1
                j += 1

    n = len(a)
    buff = [None] * n
    _merge_sort(a, 0, n-1)
    del buff