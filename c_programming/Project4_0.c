#include <stdlib.h> 
#include <stdio.h> 
#include <time.h>

#define NUM_OF_MEMBERS 5

void print_links(int data[][NUM_OF_MEMBERS] );
void matrix_multiplication(int data[][NUM_OF_MEMBERS], int result[][NUM_OF_MEMBERS] );

int main( void ) {

	int i;

	int link_data[NUM_OF_MEMBERS][NUM_OF_MEMBERS] = {0,};
	int link_result[NUM_OF_MEMBERS][NUM_OF_MEMBERS] = {0,};

	for (i=0; i<NUM_OF_MEMBERS; i++){

			link_data[i][i]=1;
	}

	link_data[0][1] = 1; link_data[1][2] = 1; link_data[2][4] = 1; link_data[3][4] = 1;

	printf("=================================================================\n");
	printf("Friends matrix\n"); 
	printf("=================================================================\n");
	print_links(link_data);

	matrix_multiplication(link_data, link_result); // 2촌 관계를 link_result에 넣는다
	
	printf("=================================================================\n");
	printf("Friends of friends matrix\n");
	printf("=================================================================\n");
	
	print_links(link_result); // 2촌까지의 관계 출력 
}
	
void print_links(int data[][NUM_OF_MEMBERS]) 
{

	int i, j; 

	for (i = 0; i < NUM_OF_MEMBERS; i++) { 
		for (j = 0; j < NUM_OF_MEMBERS; j++)  
			printf("%d ", data[i][j]);
		printf("\n");  
	}

}

void matrix_multiplication(int data[][NUM_OF_MEMBERS], int result[][NUM_OF_MEMBERS]) 
{
	int i, j;

	for(i=0; i<NUM_OF_MEMBERS; i++) {
		for(j=0; j<NUM_OF_MEMBERS; j++) {
   
			result[i][j]=data[i][0] * data[0][j] + data[i][1] * data[1][j] + data[i][2] * data[2][j] + data[i][3] * data[3][j] + data[i][4] * data[4][j];
		}
	}

}