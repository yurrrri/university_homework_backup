#include <stdio.h>
#include <stdlib.h>

int matrixPath_memo(int **m, int r, int c, int i, int j, int **M, int **M2)
{
	if (i == 0 && j == 0) {
		if (M2[0][0] == 0)
			M2[0][0] = 1;
		return m[0][0];
	}

	else if (i == 0) {
		if (M2[0][j - 1] == 0) { //값이 채워져있지 않으면,
			M[0][j - 1] = matrixPath_memo(m, r, c, 0, j - 1, M, M2);
			M2[0][j - 1] = 1; //값이 채워졌음
		}
		return M[0][j - 1] + m[i][j];
	}

	else if (j == 0) {
		if (M2[i - 1][0] == 0) {
			M[i - 1][0] = matrixPath_memo(m, r, c, i - 1, 0, M, M2);
			M2[i-1][0] = 1;
		}
		return M[i - 1][0] + m[i][j];
	}

	else {
		if (M2[i - 1][j] == 0) {
			M[i - 1][j] = matrixPath_memo(m, r, c, i - 1, j, M, M2);
			M2[i - 1][j] = 1;
		}
		if (M2[i][j - 1] == 0) {
			M[i][j - 1] = matrixPath_memo(m, r, c, i, j - 1, M, M2);
			M2[i][j-1] = 1;
		}
		return (M[i - 1][j] < M[i][j - 1] ? M[i - 1][j] : M[i][j - 1]) + m[i][j];
	}
}

int main(void) {
	int **m, **M, **M2;
	int i, j, r, c;

	printf("행 열 입력: ");
	scanf("%d %d", &r, &c);

	m = (int**)malloc(sizeof(int*) * r);
	M = (int**)malloc(sizeof(int*) * r);
	M2 = (int**)malloc(sizeof(int*)*r);

	for (i = 0; i < r; i++) {
		m[i] = (int*)malloc(sizeof(int) * c);
		M[i] = (int*)malloc(sizeof(int) * c);
		M2[i] = (int*)malloc(sizeof(int) * c);
	}

	printf("행렬 입력: ");
	for (i = 0; i < r; i++)
		for (j = 0; j < c; j++) {
			scanf("%d", &m[i][j]);
			M[i][j] = 0;
			M2[i][j] = 0;
		}

	printf("최저 점수 구하고자 하는 (i, j) 입력: ");
	scanf("%d %d", &i, &j);

	printf("(0,0) 에서 (%d,%d) 까지의 Minimum Score: %d\n", i, j, matrixPath_memo(m, r, c, i, j, M, M2));

	printf("\nMinimum Score Matrix: \n");
	for (i = 0; i < r; i++) {
		for (j = 0; j < c; j++)
			printf("%3d", M[i][j]);
		printf("\n");
	}
	printf("\n");

	for (i = 0; i < r; i++) {
		free(m[i]);
		free(M[i]);
		free(M2[i]);
	}

	free(m);
	free(M);
	free(M2);
}
