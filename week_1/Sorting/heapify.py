

def heapify(arr, i):
    
    if len(arr) > 2*i + 1:
        heapify(arr, 2*i + 1)
    if len(arr) > 2*i + 2:
        heapify(arr, 2*i + 2)

    if arr[i//2] < arr[i]:
        arr[i//2], arr[i] = arr[i], arr[i//2]

    