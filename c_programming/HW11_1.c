#include <stdio.h>

struct student{
	char name[20];
	int midterm;
	int final;
	int average;
	char grade; };

int main(void){
	struct student s[3];
	struct student *sp = s;

	int i;
	int mid_avg = 0;
	int fin_avg = 0;

	for (i=0; i<3; i++){
		printf("Enter student name: ");
		scanf("%s", sp->name);
		printf("Enter mideterm and final score: ");
		scanf("%d %d", &sp->midterm, &sp->final);
		sp->average = (sp->midterm+sp->final)/2;
		if (sp->average>=80)
			sp->grade='A';
		else if (sp->average>=50)
			sp->grade='B';
		else
			sp->grade='F';
		sp++;
	}

	sp = s;

	printf("이름	중간	학기말	평균\n");
	for (i=0; i<3; i++){
		printf("%s	%d	%d	%d\n", sp->name, sp->midterm, sp->final, sp->average);
		sp++;
	}
	printf("\n");
	printf("이름	학점\n");

	sp = s;

	for (i=0; i<3; i++){
		printf("%s	%c\n",sp->name, sp->grade);
		sp++;
	}
	printf("\n");

	sp = s;
	for (i=0; i<3; i++){
		mid_avg += sp->midterm;
		sp++;
	}
	mid_avg = mid_avg/3;

	sp = s;
	for (i=0; i<3; i++){
		fin_avg += sp->final;
		sp++;
	}
	fin_avg = fin_avg/3;

	printf("중간고사의 평균 = %d\n", mid_avg);
	printf("학기말고사의 평균 = %d\n", fin_avg);
}

