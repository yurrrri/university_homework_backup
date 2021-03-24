#include <stdio.h>

void pick(int *bucket, int itemSize, int bucketSize, int k){
	int i, lastIndex, smallest, item;

	if (k == 0) {// �� ���� ������ ���
		for (i = 0; i < bucketSize; i++)
			printf("%d ", bucket[i]);
		printf("\n");
		return;
	}

	lastIndex = bucketSize - k - 1; //picked array���� �������� ä���� element�� index
	smallest = 0;

	for (item = smallest; item < itemSize; item++) {
		bucket[lastIndex + 1] = item;
		pick(bucket, itemSize, bucketSize, k - 1);
	}
}

int main(void) {
	int num;

	printf("�� �ڸ���?: ");
	scanf("%d", &num);

	int *bucket = (int*)malloc(sizeof(int)*num);
	pick(bucket, 4, num, num);

	free(bucket);
}