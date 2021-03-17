#include<stdio.h>
int comb(int n, int r)
{
	if (n>=r)
		if (r==0 || n==r)
			return 1;
		else
			return comb(n-1, r-1) + comb(n-1, r);

}

int main(void)
{
	int C10_5;
	C10_5 = comb(10,5);
	
	return 0;
} 