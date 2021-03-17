#include <stdio.h>
#include <stdlib.h>
#include <time.h> 

int main(void)
{
	int i;
	FILE *fp1, *fp2, *fp3;
	int sum=0;
	int num;
	char buf[30];
	char ch;

	srand(time(NULL));

	fp1 = fopen("random.txt", "wt");
	if (fp1 == NULL) 
	{
		printf("file open error!\n");
		return 1;
	}

	for (i=0; i<10; i++)
		fprintf(fp1, "%d\n", rand()%100);

	fclose(fp1);

	fp2 = fopen("random.txt", "rt");
	if (fp1 == NULL) 
	{
		printf("file open error!\n");
		return 1;
	}

	fp3 = fopen("output.txt", "wt");
	if (fp3 == NULL) 
	{
		printf("file open error!\n");
		return 1;
	}

	fscanf(fp2, "%d", &num);
	while(!feof(fp2))
	{
		printf("%d\n", num);
		fprintf(fp3, "%d\n", num);
		fscanf(fp2, "%d", &num);
		sum+=num;
	}
	printf("합은 %d이다\n", sum);
	fprintf(fp3, "합은 %d이다\n", sum);

	fclose(fp2);
	fclose(fp3);
}