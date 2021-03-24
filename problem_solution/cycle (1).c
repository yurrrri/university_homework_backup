#include <stdio.h>

int get_cycle_number(int n) {
	printf("%d ", n);

	if (n == 1) {
		return 1;
	}

	else if (n % 2 == 0) 
		return 1 + get_cycle_number(n / 2);

	else
		return 1 + get_cycle_number(3 * n + 1);
}

int main(void) {
	int num;
	printf("Enter number: ");
	scanf("%d", &num);

	printf("\n사이클 길이는 %d\n", get_cycle_number(num));
}