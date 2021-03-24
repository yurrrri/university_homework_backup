#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void init_array(int list[], int n) {
	srand((unsigned)time(NULL));
	for (int i = 0; i < n; i++)
		*(list + i) = rand() % 1000;
}

void print_array(int list[], int n) {
	for (int i = 0; i < n; i++)
		printf("%3d ", list[i]);
}


void selection_sort(int list[], int n) {
	int i, j;

	for (i = 0; i < n - 1; i++) {
		int max = list[0];
		int max_idx = 0;

		for (j = 1; j < n-i ; j++) {
			if (max < list[j]) {
				max = list[j];
				max_idx = j;
			}
		}
		int num = list[n - i - 1];
		list[max_idx] = num;
		list[n - i - 1] = max;
	}
}

int main(void) {
	int num;
	int *p;
	printf("Enter a number: ");
	scanf("%d", &num);

	p = (int*)malloc(sizeof(int) * num);

	init_array(p, num);
	print_array(p, num);

	selection_sort(p, num);
	printf("\n정렬된 후:\n");
	print_array(p, num);

	free(p);
}