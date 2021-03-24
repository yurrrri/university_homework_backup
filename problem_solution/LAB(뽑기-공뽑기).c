#include <stdio.h>

void pick(char items[], int itemSize, int bucket[], int bucketSize, int k){
	int i, lastIndex, smallest, item;

	if (k == 0) { // �� ���� ������ ���
		for (i = 0; i < bucketSize; i++)
			printf("%c ", items[bucket[i]]);
		printf("\n");
		return;
	}

	lastIndex = bucketSize - k - 1; //picked array���� �������� ä���� element�� index

	if (bucketSize == k) // ó�� ���� �Ÿ�
		smallest = 0;
	else
		smallest = bucket[lastIndex] + 1;

	for (item= smallest; item <itemSize; item++) {
		bucket[lastIndex + 1] = item;
		pick(items, itemSize, bucket, bucketSize, k - 1);
	}
}

int main(void) {
	int picked[3];
	char items[7] = { 'A', 'B', 'C', 'D', 'E', 'F', 'G' };
	pick(items,7, picked, 3, 3);
}