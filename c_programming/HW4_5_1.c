#include<stdio.h>

int get_cycle_number(int n){
	
	int count = 0;

	while (1){
		count ++;

		if (n==1)
			break;
		if ((n%2)==0)
			n = n/2;
		else
			n = n*3 +1;

		printf("%d ", n);
	}

	return count;
}


int main(void){

	int n;
	printf("���ڸ� �Է��Ͻÿ� :");
	scanf("%d", &n);

	get_cycle_number(n);

	return 0;

}