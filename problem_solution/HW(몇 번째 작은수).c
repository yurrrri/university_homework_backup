#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void init_array(int list[], int n) {
	srand(time(NULL));
	for (int i = 0; i < n; i++)
		*(list + i) = rand() % 100;
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

int find(int A[], int p, int r, int orderIndex) {
	int q;

	if (p <= r) {
		q = partition(A, p, r);

		if (orderIndex == q)
			return A[orderIndex];
		else if (orderIndex < q)
			find(A, p, q - 1, orderIndex);
		else
			find(A, q + 1, r, orderIndex);
	}
}

int main(void) {
	int num, order;
	int *list;

	printf("Enter the number of numbers: ");
	scanf("%d", &num);

	printf("몇번째로 작은 수: ");
	scanf("%d", &order);

	list = (int*)malloc(sizeof(int) * num);

	init_array(list, num);
	print_array(list, num);

	int order_num = find(list, 0, num - 1, order-1);
	printf("\n%d번째 작은 수는 : %d\n", order, order_num);

	free(list);
}