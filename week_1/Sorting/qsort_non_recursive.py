from typing import MutableSequence
from stack_10828 import MyStack

def quick_sort_non_recursive(arr : MutableSequence, l : int, r: int) -> None:
    range = MyStack(r - l + 1)
    range.push((l, r))
    
    while not range.empty():
        pl, pr = l, r = range.pop()
        x = arr[(l + r) // 2]

        while pl <= pr:
            while arr[pl] < x : pl += 1
            while arr[pr] > x : pr -= 1
            if pl <= pr:
                arr[pl], arr[pr] = arr[pr], arr[pl]
                pl += 1
                pr -= 1
        
        if l < pr : range.push((l, pr))
        if pl < r : range.push((pl. r))


N = int(input())
arr = []
while N > 0:
    N -= 1
    arr.append(int(input()))

quick_sort_non_recursive(arr)

for i in arr:
    print(i)