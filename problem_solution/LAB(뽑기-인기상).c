#include <stdio.h>

void pick(char list[][7], int itemSize, int* bucket, int bucketSize, int k){
	int i, lastIndex, smallest, item;

	if (k == 0) {// 고를 것이 없으면 출력
		for (i = 0; i < bucketSize; i++)
			printf("%10s", list[bucket[i]]);
		printf("\n");
		return;
	}

	lastIndex = bucketSize - k - 1; //picked array에서 마지막에 채워진 element의 index

	if (bucketSize == k) // 처음 고르는 거면
		smallest = 0;
	else
		smallest = bucket[lastIndex] + 1;

	for (item = smallest; item < itemSize; item++) {
		bucket[lastIndex + 1] = item;
		pick(list, itemSize, bucket, bucketSize, k - 1);
	}
}

int main(void) {
	char actors[][7] = { "공유", "김수현", "송중기", "지성", "현빈" };
	int num;

	printf("인기상 몇명? ");
	scanf("%d", &num);

	int *bucket = (int*)malloc(sizeof(int)*num);

	pick(actors, 5, bucket, num, num);

	free(bucket);
}