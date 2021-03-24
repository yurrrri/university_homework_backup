#include <stdio.h>
#include <stdlib.h>

int pick(int *items, int itemsize, int* bucket, int bucketSize, int k, int money) {
	int i, lastIndex, smallest, j;
	int sum = 0;
	int count = 0;

	lastIndex = bucketSize - k - 1; // 가장 최근에 뽑힌 수가 저장된 위치 index

	// 여지까지 bucket에 든 액수를 sum으로 계산
	for (i = 0; i <= lastIndex; i++)
		sum += bucket[i];

	if (sum == money) {
		for (i = 0; i <= lastIndex; i++)
			printf("%d ", bucket[i]);
		printf("\n");
		return 1;
	}

	if (sum > money) // 효율성을 위해!!
		return 0;

	if (bucketSize == k)
		smallest = items[0];
	else
		smallest = bucket[lastIndex]; // 다음에 넣을 돈

	// bucket에 items의 원소들을 넣으면서 재귀 호출...
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
	int items[] = { 1000, 5000, 10000 };
	int *bucket;
	int money, n;

	scanf("%d", &money);
	n = money / 1000;
	bucket = (int *)malloc(sizeof(int) * n);

	printf("%d\n", pick(items, 3, bucket, n, n, money));
}