#include <stdio.h>
#include <ctype.h>

int main(void)
{
	char ch1, ch2;
	FILE *fp1, *fp2;

	fp1 = fopen("input.txt", "rt");
	if (fp1 == NULL) 
	{
		printf("file open error!\n");
		return 1;
	}

	fp2 = fopen("output.txt", "wt");
	if (fp2 == NULL) 
	{
		printf("file open error!\n");
		return 1;
	}

	ch1 = getc(fp1);
	while (!feof(fp1)){
		if (islower(ch1)){
			putc(toupper(ch1), fp2);
		}
		else{
			putc(ch1, fp2);
		}
		ch1 = getc(fp1);
	}
	fprintf(fp2, "\n\n");

	fseek(fp1, 0, SEEK_SET);

	ch2 = getc(fp1);
	while (!feof(fp1)){
		if (isupper(ch2)){
			putc(tolower(ch2), fp2);
		}
		else{
			putc(ch2, fp2);
		}
		ch2 = getc(fp1);
	}

	fclose(fp1);
	fclose(fp2);
}