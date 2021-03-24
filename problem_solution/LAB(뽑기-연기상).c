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

	smallest = 0;

	for (item = smallest; item < itemSize; item++) {
		int chosen = 0;

		for (int j = -1; j <= lastIndex; j++) {
			if (bucket[j] == item) {
				chosen = 1;
				break;
			}
		}

		if (chosen) 
			continue;

		bucket[lastIndex + 1] = item;
		pick(list, itemSize, bucket, bucketSize, k - 1);
	}
}

int main(void) {
	char actors[][7] = { "����", "�����", "���߱�", "����", "����" };
	int num;

	printf("���� ������? ");
	scanf("%d", &num);

	for (int i = 0; i < num; i++) 
		printf("%8s %d", "��", i + 1);

	printf("\n");

	int *bucket = (int*)malloc(sizeof(int)*num);

	pick(actors, 5, bucket, num, num);

	free(bucket);
}