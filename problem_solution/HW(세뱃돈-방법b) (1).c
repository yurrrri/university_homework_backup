#include <stdio.h>
#include <stdlib.h>

int pick(int *items, int itemsize, int* bucket, int bucketSize, int k, int money) {
	int i, lastIndex, smallest, j;
	int sum = 0;
	int count = 0;

	if (k == 0) {
		for (i = 0; i < bucketSize; i++)
			sum += bucket[i];
		if (sum == money) {
			for (i = 0; i < bucketSize; i++) {
				if (bucket[i] == 0) {
					continue;
				}
				printf("%d ", bucket[i]);
			}
		}
		else
			return 0;
		printf("\n");
		return 1;
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
		count += pick(items, itemsize, bucket, bucketSize, k - 1, money);
	}
	return count;
}

int main(void)
{
	int items[] = { 0, 1000, 5000, 10000 };
	int *bucket;
	int money, n;

	scanf("%d", &money);
	n = money / 1000;
	bucket = (int *)malloc(sizeof(int) * n);

	printf("%d\n", pick(items, 4, bucket, n, n, money));
}