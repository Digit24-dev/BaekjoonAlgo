#include <stdio.h>
#include <stdlib.h>

#define MAX_ELEMENT 100

typedef struct {
	int heap[MAX_ELEMENT];
	int heap_size;
} heapType;

heapType* createHeap() {
	heapType* h = (heapType*)malloc(sizeof(heapType));
	h->heap_size = 0;
	return h;
}

// 힙에 item을 삽입하는 연산
void insertHeap(heapType* h, int item) {
	int i;
	h->heap_size = h->heap_size + 1;
	i = h->heap_size;

	while ((i != 1) && (item > h->heap[i / 2])) {
		h->heap[i] = h->heap[i / 2];
		i /= 2;
	}
	h->heap[i] = item;
}

// 힙의 루트를 삭제하여 반환하는 연산
int deleteHeap(heapType* h) {
	int item = h->heap[1];
	int temp = h->heap[h->heap_size];
	h->heap_size--;

	int j = 2, i = 1;
	while (j <= h->heap_size && h->heap[j] > temp) {
		if (j < h->heap_size && h->heap[j] < h->heap[j + 1]) j++;
		if (temp >= h->heap[j]) break;
		else {
			h->heap[i] = h->heap[j];
			i = j;
			j = j * 2;
		}
	}
	h->heap[i] = temp;

	return item;
}

void printHeap(heapType* h) {
	int i;
	printf("Heap : ");
	for (i = 1; i <= h->heap_size; i++) {
		printf("[%d] ", h->heap[i]);
	}
}

int main() {

	int i, n, item;
	heapType* heap = createHeap();
	insertHeap(heap, 10);
	insertHeap(heap, 45);
	insertHeap(heap, 19);
	insertHeap(heap, 11);
	insertHeap(heap, 96);

	printHeap(heap);

	n = heap->heap_size;
	for (i = 1; i <= n; i++) {
		item = deleteHeap(heap);
		printf("\n delete : [%d] ", item);
	}
	getchar();
	return 0;
}