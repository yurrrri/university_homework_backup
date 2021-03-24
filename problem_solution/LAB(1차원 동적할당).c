#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int init_array(int list[], int n) {
	srand((unsigned)time(NULL));

	for (int i = 0; i < n; i++)
		*(list+i) = rand() % 1000;
}

void print_array(int list[],int n) {
	for (int i = 0; i < n; i++)
		printf("%3d ", list[i]);
}

int main(void) {
	int num;
	int *p;
	printf("Enter a number: ");
	scanf("%d", &num);

	p = (int*)malloc(sizeof(int) * num);

	init_array(p, num);
	print_array(p, num);

	free(p);
}