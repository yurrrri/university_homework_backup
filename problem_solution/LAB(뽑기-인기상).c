#include <stdio.h>

void pick(char list[][7], int itemSize, int* bucket, int bucketSize, int k){
	int i, lastIndex, smallest, item;

	if (k == 0) {// �� ���� ������ ���
		for (i = 0; i < bucketSize; i++)
			printf("%10s", list[bucket[i]]);
		printf("\n");
		return;
	}

	lastIndex = bucketSize - k - 1; //picked array���� �������� ä���� element�� index

	if (bucketSize == k) // ó�� ���� �Ÿ�
		smallest = 0;
	else
		smallest = bucket[lastIndex] + 1;

	for (item = smallest; item < itemSize; item++) {
		bucket[lastIndex + 1] = item;
		pick(list, itemSize, bucket, bucketSize, k - 1);
	}
}

int main(void) {
	char actors[][7] = { "����", "�����", "���߱�", "����", "����" };
	int num;

	printf("�α�� ���? ");
	scanf("%d", &num);

	int *bucket = (int*)malloc(sizeof(int)*num);

	pick(actors, 5, bucket, num, num);

	free(bucket);
}