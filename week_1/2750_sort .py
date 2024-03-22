import sys

N = int(sys.stdin.readline())

arr = []

for _ in range(0, N):
    n = int(sys.stdin.readline())
    arr.append(n)

# arr = sorted(arr)

# bubble sort
# for i in range(0, N):
#     for j in range(i + 1, N):
#         if arr[i] > arr[j]:
#             temp = arr[i]
#             arr[i] = arr[j]
#             arr[j] = temp

# insertion sort
for key in range(0, N):
    for idx in range(key, 0, -1):
        if arr[idx - 1] > arr[idx]:
            arr[idx - 1], arr[idx] = arr[idx], arr[idx - 1]


# merge sort
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    # divide
    mid = len(arr) // 2
    
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # end divide
    
    # conquer
    merged_arr = []
    if left > right:
        merged_arr.append(left, right)

if:

print('=========')

for i in arr:
    print(i)