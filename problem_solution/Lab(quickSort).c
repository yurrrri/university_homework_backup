#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void init_array(int list[], int n) {
	srand(time(NULL));
	for (int i = 0; i < n; i++)
		*(list + i) = rand() % 1000;
}

void print_array(int list[], int n) {
	for (int i = 0; i < n; i++)
		printf("%3d ", list[i]);
}

void swap(int A[], int i, int j) {
	int temp = A[j];
	A[j] = A[i];
	A[i] = temp;
}

int partition(int A[], int p, int r) {
	int i = p - 1;
	int j = p;
	int pivot = A[r];

	while (j < r) {
		if (A[j] < pivot) {
			swap(A, ++i, j);
		}
		j++;
	}
	swap(A, ++i, j);

	r = i;
	return r;
}

void quick_sort(int list[], int p, int r) {
	int q;
	
	if (p < r) {
		q = partition(list, p, r);
		quick_sort(list, p, q - 1);
		quick_sort(list, q + 1, r);
	}
}

int main(void) {
	int num;
	int *list;

	printf("Enter a number: ");
	scanf("%d", &num);

	list = (int*)malloc(sizeof(int) * num);

	init_array(list, num);
	print_array(list, num);

	quick_sort(list, 0, num-1);
	printf("\n정렬된 후:\n");
	print_array(list, num);

	free(list);
}