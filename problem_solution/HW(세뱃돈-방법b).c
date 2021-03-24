#include <stdio.h>
#include <stdlib.h>

void pick(int *items, int itemsize, int* bucket, int bucketSize, int k, int money) {
	int i, lastIndex, smallest, j;
	int sum = 0;

	if (k == 0) {
		for (i = 0; i < bucketSize; i++)
			sum += bucket[i];
		if (sum == money) {
			for (i = 0; i < bucketSize; i++) {
				if (bucket[i] == 0)
					continue;
				printf("%d ", bucket[i]);
			}
		}
		else
			return;
		printf("\n");
		return;
	}

	lastIndex = bucketSize - k - 1; // ���� �ֱٿ� ���� ���� ����� ��ġ index

	if (bucketSize == k)
		smallest = 0;
	else
		smallest = bucket[lastIndex]; // �ߺ�����!!

	// bucket�� items�� ���ҵ��� �����鼭 ��� ȣ��...
	for (j = 0; j < itemsize; j++) {
		if (items[j] == smallest)
			break;
	}

	for (i = j; i < itemsize; i++) {
		bucket[lastIndex + 1] = items[i];
		pick(items, itemsize, bucket, bucketSize, k - 1, money);
	}
}

int main(void)
{
	int items[] = { 0, 1000, 5000, 10000 };
	int *bucket;
	int money, n;

	scanf("%d", &money);
	n = money / 1000;
	bucket = (int *)malloc(sizeof(int) * n);

	pick(items, 4, bucket, n, n, money);
}