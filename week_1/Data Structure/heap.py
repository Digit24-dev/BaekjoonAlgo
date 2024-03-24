class HeapType:
    def __init__(self):
        self.heap = []
        self.heap_size = 0

def createHeap():
    h = HeapType()
    h.heap_size = 0
    return h

def insertHeap(h, item):
    h.heap_size += 1
    i = h.heap_size
    while i != 1 and item > h.heap[i // 2]:
        h.heap[i] = h.heap[i // 2]
        i //= 2
    h.heap[i] = item

def deleteHeap(h):
    item = h.heap[1]
    temp = h.heap[h.heap_size]
    h.heap_size -= 1
    j = 2
    i = 1
    while j <= h.heap_size and h.heap[j] > temp:
        if j < h.heap_size and h.heap[j] < h.heap[j + 1]:
            j += 1
        if temp >= h.heap[j]:
            break
        else:
            h.heap[i] = h.heap[j]
            i = j
            j = j * 2
    h.heap[i] = temp
    return item

def printHeap(h):
    print("Heap: ", end="")
    for i in range(1, h.heap_size + 1):
        print("[%d] " % h.heap[i], end="")

heap = createHeap()
insertHeap(heap, 10)
insertHeap(heap, 45)
insertHeap(heap, 19)
insertHeap(heap, 11)
insertHeap(heap, 96)
printHeap(heap)
n = heap.heap_size
for i in range(1, n + 1):
    item = deleteHeap(heap)
    print("\n delete: [%d] " % item, end="")

