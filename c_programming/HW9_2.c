#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>


int main(void){
	char string[50];
	char year[50]="19";

	printf("�ֹε�Ϲ�ȣ �Է�<'-'����>:");
	gets(string);
	strncat(year, string, 2);
	printf("����� %s�⵵ ���̱���\n", year);

	if (string[7]=='2'){
		printf("���ں��̽ñ���\n");
		printf("��� ���� 84�� ���ϸ� %d���� ��ٰ� ���˴ϴ�\n", atoi(year)+84);
	}
	else if (string[7]=='1'){
		printf("���ں��̽ñ���\n");
		printf("��� ���� 77�� ���ϸ� %d���� ��ٰ� ���˴ϴ�\n", atoi(year)+77);
	}




}