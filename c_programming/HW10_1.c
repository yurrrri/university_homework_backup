#include <stdio.h>

struct student{
	char name[20];
	int midterm;
	int final;
	int average;
	char grade; };

int main(void){
	struct student s[3];
	int i;

	for (i=0; i<3; i++){
		printf("Enter student name: ");
		scanf("%s", s[i].name);
		printf("Enter mideterm and final score: ");
		scanf("%d %d", &s[i].midterm, &s[i].final);
		s[i].average = (s[i].midterm+s[i].final)/2;
		if (s[i].average>=80)
			s[i].grade='A';
		else if (s[i].average>=50)
			s[i].grade='B';
		else
			s[i].grade='F';
	}

	
	printf("�̸�	�߰�	�б⸻	���\n");
	for (i=0; i<3; i++)
		printf("%s	%d	%d	%d\n", s[i].name, s[i].midterm, s[i].final, s[i].average);
	printf("\n");
	printf("�̸�	����\n");
	for (i=0; i<3; i++)
		printf("%s	%c\n",s[i].name, s[i].grade);
	printf("\n");
	printf("�߰������ ��� = %d\n", (s[0].midterm+s[1].midterm+s[2].midterm)/3);
	printf("�б⸻����� ��� = %d\n", (s[0].final+s[1].final+s[2].final)/3);
}

