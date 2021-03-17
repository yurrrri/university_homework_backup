#include <stdio.h> 
int printArray(int arr[][4], int size) {
	int i, j; 

	for (i = 0; i < size; i++) { 
		for (j = 0; j < 4; j++)  
			printf("%d ", arr[i][j]);
		printf("\n");  
	} 

	return 0;
}

int main(void) {
	int i, j;
	int k=0;
	int a[4][4], b[4][4], c[4][4], d[4][4]; 

	for (i = 0; i < 4; i++) 
		for (j = 0; j < 4; j++) {
			a[i][j] = k+1;
			k++;
		}

	printArray(a, 4); printf("\n");

	for (i = 0; i < 4; i++) 
		for (j = 0; j < 4; j++) { 
			b[j][3-i] = a[i][j];
		}

	printArray(b, 4); printf("\n");

	for (i = 0; i < 4; i++) 
		for (j = 0; j < 4; j++) {
			c[j][3-i] = b[i][j];
		}

	printArray(c, 4); printf("\n");

	for (i = 0; i < 4; i++) 
		for (j = 0; j < 4; j++) {
			d[j][3-i] = c[i][j];
		}

	printArray(d, 4); printf("\n");

	printArray(a, 4); printf("\n");


} 