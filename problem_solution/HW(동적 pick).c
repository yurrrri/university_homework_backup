#include <stdio.h>

void pick(int n, int picked[], int m, int toPick) {
	int smallest, lastIndex, i;
	if (toPick == 0) {// �� ���� ������ ���
		for (i = 0; i < m; i++)
			printf("%d ", picked[i]);
		printf("\n");
		return;
	}

	lastIndex = m - toPick - 1; //picked array���� �������� ä���� element�� index

	if (m == toPick) // ó�� ���� �Ÿ� 
		smallest = 0;
	else
		smallest = picked[lastIndex] + 1;

	for (i = smallest; i < n; i++) {
		picked[lastIndex + 1] = i;
		pick(n, picked, m, toPick - 1);
	}
}

int main(void) {
	int n, m;
	int *picked;

	printf("Enter n and m:");
	scanf("%d %d", &n, &m);

	picked = (int*)malloc(sizeof(int) * m);

	pick(n, picked, m, m);

	free(picked);
}