#include <stdio.h>
#define x_player 0
#define y_player 1

void display(char b[][10], int count, int su1, int su2){

	int i, j;

	printf("    ----------------------\n");
	printf("    0 1 2 3 4 5 6 7 8 9 \n");

	if (count==0)
		b[su1][su2] = 'X';
	else
		b[su1][su2] = 'O';

	for (i=0; i<10; i++)
		printf("%d : \n", i);
		for (j=0; j<10; j++)
			printf("%c", b[i][j]);
}

int main(void){
	int i;
	int count=0;
	int su1=0, su2=0;
	char arr[10][10];

	printf("    ----------------------\n");
	printf("    0 1 2 3 4 5 6 7 8 9 \n");
	for (i=0; i<10; i++)
		printf("%d : \n", i);

	while (1){
		if (count==x_player){
			printf("Player X<행 열>:");
			scanf("%d %d", &su1, &su2);
			printf("\n");
			count = 1;
		}
		else if (count==y_player){
			printf("Player Y<행 열>: \n");
			scanf("%d %d", &su1, &su2);
			printf("\n");
			count = 0;
		}
		display(arr, count, su1, su2);
		printf("\n");
	}
}