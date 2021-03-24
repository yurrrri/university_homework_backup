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


void bubble_sort(int list[], int n) {
	int i, j;

	for (i = 0; i < n - 1; i++) {
		for (j = 0; j < n - i - 1; j++) {
			if (list[j] > list[j + 1]) {
				int large = list[j];
				list[j] = list[j + 1];
				list[j + 1] = large;
			}
		}
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

	bubble_sort(p, num);
	printf("\n정렬된 후:\n");
	print_array(p, num);

	free(p);
}