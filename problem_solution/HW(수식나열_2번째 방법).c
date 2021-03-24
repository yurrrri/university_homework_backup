#include <stdio.h>
#include <stdlib.h>
void pick(int *items, int itemSize, int* bucket, int bucketSize, int k) {
	int i, lastIndex, smallest;
	int total = 0;

	if (k == 0) {
		// �ڵ� �߰�
		for (int i = 0; i < bucketSize; i++) {
			switch (bucket[i]) {
			case 1:
				printf("+%d", i + 1);
				total += i + 1;
				break;
			case -1:
				printf("-%d", i + 1);
				total -= i + 1;
				break;
			}
		}
		printf("=%d\n", total);
		return;
	}

	lastIndex = bucketSize - k - 1; // ���� �ֱٿ� ���� ���� ����� ��ġ i

	smallest = 0; // �ߺ�����	
	for (i = smallest; i < itemSize; i++) {
		bucket[lastIndex + 1] = items[i];
		pick(items, itemSize, bucket, bucketSize, k - 1);
	}
}
int main(void)
{
	int items[] = { 1, -1 }; // Ȥ�� char items[] = {'+', '-'};
	int *bucket;
	int n;

	printf("���� �Է�: ");
	scanf("%d", &n);

	bucket = (int *)malloc(sizeof(int) * n);
	pick(items, 2, bucket, n, n);
}
