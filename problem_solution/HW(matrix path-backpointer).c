#include <stdio.h>
#include <stdlib.h>

#define LE 1 //왼쪽
#define UP 2 //위쪽

int matrixPath_memo(int **m, int r, int c, int i, int j, int **M, int **BP)
{
	if (i == 0 && j == 0)
		return m[0][0];

	else if (i == 0) {
		BP[i][j] = LE;

		if (M[0][j - 1] == 0)
			M[0][j - 1] = matrixPath_memo(m, r, c, 0, j - 1, M, BP);
		return M[0][j - 1] + m[i][j];
	}

	else if (j == 0) {
		BP[i][j] = UP;

		if (M[i - 1][0] == 0)
			M[i - 1][0] = matrixPath_memo(m, r, c, i - 1, 0, M, BP);
		return M[i - 1][0] + m[i][j];
	}

	else {
		if (M[i - 1][j] == 0)
			M[i - 1][j] = matrixPath_memo(m, r, c, i - 1, j, M, BP);
		if (M[i][j - 1] == 0)
			M[i][j - 1] = matrixPath_memo(m, r, c, i, j - 1, M, BP);

		BP[i][j] = M[i - 1][j] < M[i][j - 1] ? UP : LE;
		return (M[i - 1][j] < M[i][j - 1] ? M[i - 1][j] : M[i][j - 1]) + m[i][j];
	}
}

void print_path(int i, int j, int **BP) {
	if (BP[i][j] == UP)
		print_path(i - 1, j, BP);
	else if (BP[i][j] == LE)
		print_path(i, j - 1, BP);

	printf("<%d,%d> ", i, j);
}

int main(void) {
	int **m, **M, **BP; // M은 메모, BP는 backpointer
	int i, j, r, c;

	printf("행 열 입력: ");
	scanf("%d %d", &r, &c);

	m = (int**)malloc(sizeof(int*) * r);
	M = (int**)malloc(sizeof(int*) * r);
	BP = (int**)malloc(sizeof(int*) * r);

	for (i = 0; i < r; i++) {
		m[i] = (int*)malloc(sizeof(int) * c);
		M[i] = (int*)malloc(sizeof(int) * c);
		BP[i] = (int*)malloc(sizeof(int) * c);
	}

	printf("행렬 입력: ");
	for (i = 0; i < r; i++)
		for (j = 0; j < c; j++) {
			scanf("%d", &m[i][j]);
			M[i][j] = 0; //메모 초기화
			BP[i][j] = 0;
		}

	printf("최저 점수 구하고자 하는 (i, j) 입력: ");
	scanf("%d %d", &i, &j);

	printf("(0,0) 에서 (%d,%d) 까지의 Minimum Score: %d\n", i, j, matrixPath_memo(m, r, c, i, j, M, BP));

	printf("\nMinimum Score Matrix: \n");
	for (i = 0; i < r; i++) {
		for (j = 0; j < c; j++)
			printf("%3d", M[i][j]);
		printf("\n");
	}
	printf("\n");

	printf("BackPointer Matrix: \n");
	for (i = 0; i < r; i++) {
		for (j = 0; j < c; j++)
			printf("%3d", BP[i][j]);
		printf("\n");
	}
	printf("\n");

	printf("minimum score matrix path: \n");
	print_path(r - 1, c - 1, BP);

	for (i = 0; i < r; i++) {
		free(m[i]);
		free(M[i]);
		free(BP[i]);
	}

	free(m);
	free(M);
	free(BP);
}
