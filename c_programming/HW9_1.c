#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
	int i=0; 
	int j=0;

	char string[50]; // �ԷµǴ� ���ڿ��� ����
	char alphaString1[50]; // �Է¹��ڿ����� ���ĺ��� ����
	char alphaString2[50]; // ��ҹ��ڸ� �ٲ�
	char digitString[50];
	char convertedString[50]; // ���ڵ�� ���ڵ�� ��迭�� ���ڿ�
	
	printf("���ڿ��� �Է��ϼ���:");
	gets(string);
	for (i=0; string[i]!='\0'; i++){
		if (isalpha(string[i]))
			alphaString1[j++] = string[i];
	}
	alphaString1[j]='\0';

	j=0;
	for (i=0; string[i]!='\0'; i++){
		if (isdigit(string[i]))
			digitString[j++] = string[i];
	}
	digitString[j] = '\0';
	printf("���ڵ��� %s\n", alphaString1);
	printf("���ڵ��� %s\n", digitString);

	j=0;
	for (i=0; alphaString1[i]!='\0'; i++){
		if (islower(alphaString1[i]))
			alphaString2[j++] = toupper(alphaString1[i]);
		else if (isupper(alphaString1[i]))
			alphaString2[j++] = tolower(alphaString1[i]);
	}
	alphaString2[j]='\0';

	strcpy(convertedString, strcat(alphaString1, digitString));

	printf("��ҹ��ڸ� �ٲ� ���ڵ��� %s\n", alphaString2);
	printf("���ڵ�� ���ڵ�� ��迭�� ���ڿ��� %s\n", convertedString);
} 