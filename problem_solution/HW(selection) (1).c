#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct Student {
	int id;
	int korean, english, math;
} Student;

void init_score(Student *p, int n) {
	srand((unsigned)time(NULL));

	for (int i = 0; i < n; i++) {
		p->id = i + 1;
		p->korean = rand() % 101;
		p->english = rand() % 101;
		p->math = rand() % 101;
		p++;
	}
}

void print_score(Student *p, int n) {
	for (int i = 0; i < n; i++) {
		printf("학번 : %d		국어 : %d		영어 : %d		수학 : %d\n", p->id, p->korean, p->english, p->math);
		p++;
	}
}

void selection_sort(Student *p, int n) {
	int i, j;
	Student num;

	for (i = 0; i < n-1; i++) {
		int max = p[i].korean;
		int max_idx = i;

		for (j = i+1; j < n ; j++) {
			if (max < p[j].korean) {
				max = p[j].korean;
				max_idx = j;
			}
		}
		num = p[max_idx];
		p[max_idx] = p[i];
		p[i] = num;
	}
}

int main(void) {
	int n;
	Student *p;

	printf("학생 수를 입력하세요 : ");
	scanf("%d", &n);

	p = (Student*) malloc(sizeof(Student) * n);

	init_score(p, n);
	print_score(p, n);

	selection_sort(p, n);

	printf("\n정렬된 후:\n");
	print_score(p, n);

	free(p);
}