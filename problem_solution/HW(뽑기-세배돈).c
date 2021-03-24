#pragma warning(disable:4996)
#include <stdio.h>
#include <stdlib.h>

int pick(int money, int *bills, int itemSize, int *picked, int bucketSize, int k) {
	int i, lastIndex, smallest, item;
	int sum = 0;
	int count = 0;

	if (k == 0) {
		for (i = 0; i < bucketSize; i++)
			sum += bills[picked[i]];
		if (sum == money) {
			for (i = 0; i < bucketSize; i++) {
				if (bills[picked[i]] == 0) {
					continue;
				}
				printf("%d ", bills[picked[i]]);
			}
		}
		else
			return 0;
		printf("\n");
		return 1;
	}

	lastIndex = bucketSize - k - 1;

	if (bucketSize == k)
		smallest = 0;
	else
		smallest = picked[lastIndex];

	for (item = smallest; item < itemSize; item++) {
		picked[lastIndex + 1] = item;
		count += pick(money, bills, itemSize, picked, bucketSize, k - 1);
	}
	return count;
}

int main(void) {
	int money, n;

	scanf("%d", &money);

	int bills[4] = { 0, 1000, 5000, 10000 };
	n = money / 1000;

	int *picked = (int*)malloc(sizeof(int)*n);

	printf("%d\n", pick(money, bills, 4, picked, n, n));

	free(picked);
}