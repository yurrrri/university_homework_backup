#include<stdio.h>

int get_cycle_number(int n){

	int count = 0;
	count++;

	if (n==1){
		return;
	}
	else if (n%2 ==0){
		printf("%d ", n/2);
		return get_cycle_number(n/2);
	}
	else{
		printf("%d ", n*3 + 1);
		return get_cycle_number(n*3+1);
	}
	
	return count;
}


int main(void){

	int n;

	printf("���ڸ� �Է��ϼ���: ");
	scanf("%d", &n);

	get_cycle_number(n);

}