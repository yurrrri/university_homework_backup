#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
	int i=0; 
	int j=0;

	char string[50]; // 입력되는 문자열을 저장
	char alphaString1[50]; // 입력문자열에서 알파벳만 저장
	char alphaString2[50]; // 대소문자를 바꿈
	char digitString[50];
	char convertedString[50]; // 문자들과 숫자들로 재배열한 문자열
	
	printf("문자열을 입력하세요:");
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
	printf("문자들은 %s\n", alphaString1);
	printf("숫자들은 %s\n", digitString);

	j=0;
	for (i=0; alphaString1[i]!='\0'; i++){
		if (islower(alphaString1[i]))
			alphaString2[j++] = toupper(alphaString1[i]);
		else if (isupper(alphaString1[i]))
			alphaString2[j++] = tolower(alphaString1[i]);
	}
	alphaString2[j]='\0';

	strcpy(convertedString, strcat(alphaString1, digitString));

	printf("대소문자를 바꾼 문자들은 %s\n", alphaString2);
	printf("문자들과 숫자들로 재배열한 문자열은 %s\n", convertedString);
} 