#include <stdio.h>

int H(int i) {

	int sum = 0;

	if (i == 0 || i == 1) {
		return 1;
	}
	else {
		for (int n = 0; n < i; n++) 
			sum += H(n)*H(i - n - 1);
		return sum;
	}
}

int main(void) {
	int i, num;
	printf("i�� �Է��ϼ���: ");
	scanf("%d", &num);

	for (i = 0; i <= num; i++)
		printf("i = %d�� �� %d\n", i, H(i));
}