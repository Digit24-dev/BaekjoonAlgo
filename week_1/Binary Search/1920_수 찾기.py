import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))

a = sorted(a)

def binarySearch(arr, key):
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if key == arr[mid]:
            return 1
        
        if key > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return 0

for i in b:
    print(binarySearch(a, i))