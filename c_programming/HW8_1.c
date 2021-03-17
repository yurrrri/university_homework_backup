#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int sumUpData(int *, int);
void printData(int *, int);
int maxData(int *, int);

void main()
{
	int k;
	int *p;
	int sum;
	
	int data[10]; // ��� ���࿡ ����� ���� ����
	p = data; //Ȥ�� p = &data[0]

	srand(time(NULL)); // random �� ��¿� ����ϴ� �Լ�. Seed ���� �ο�
	for (k = 0; k < 10; k++) // Index 0..9����
		*p++ = rand() % 100; // ������ �ʱ�ȭ. 0���� 99������ Random ���� ���.
	
	sum = sumUpData(data, 10);
	printf("������Ʈ�� ���� %d\n", sum);
	printf("������Ʈ���� ");
	printData(data, 10);
	printf("\n������Ʈ�� �� ���� ū���� %d \n", maxData(data, 10));
}

int sumUpData(int *p, int size) // int p[]�� �ᵵ �ȴ�
{
	int k;
	int sum=0;

	for (k=0; k<size; k++)
		sum+=*(p+k);
	return sum;
}
void printData(int *p, int size) // int p[]�� �ᵵ �ȴ�
{
	int k;
	for (k=0; k<size; k++)
		printf("%d ", *(p+k));
}
int maxData(int *p, int size) // int p[]�� �ᵵ �ȴ�
{
	int max=0;
	int k;
	for (k=0; k<size; k++){
		if (max<*(p+k))
			max = *(p+k);
	}

	return max;
} 