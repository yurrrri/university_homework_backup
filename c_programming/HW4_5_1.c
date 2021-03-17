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
	printf("숫자를 입력하시오 :");
	scanf("%d", &n);

	get_cycle_number(n);

	return 0;

}