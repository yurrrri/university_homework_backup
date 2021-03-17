#include <stdio.h>
#define BOARD_SIZE 10
int winCheck(char b[][BOARD_SIZE], int r, int c)
{
	char player=b[r][c];
	int sum=0;
	int i=0;

	while (b[r][c-i]==player && c-i>=0){
		i++;
		sum++;
	}
	while (b[r][c+i]==player && c+i<BOARD_SIZE){
		i++;
		sum++;
	}
	while (b[r-i][c] == player && r - i >= 0){
		i++;
		sum++;
	}
	while (b[r+i][c] == player && r+i < BOARD_SIZE){
		i++;
		sum++;
	}
	while (b[r-i][c+i] == player && r-i>=0 && c+i <BOARD_SIZE){
		i++;
		sum++;
	}
	while (b[r-i][c-i] == player && r-i>=0 && c-i >=0){
		i++;
		sum++;
	}

	if (sum==5)
		return 1;

	return 0;
}

void display(char b[][BOARD_SIZE])
{
	int i, j;
	printf("     ");
	for (i=0; i<BOARD_SIZE; i++)
		printf("%2d", i);
	printf("\n     --------------------\n");
	for (i=0; i<BOARD_SIZE; i++){
		printf("%3d |", i);
		for (j=0; j<BOARD_SIZE; j++)
			printf(" %c", b[i][j]);
		printf("\n");
	}
}

int main(void)
{
	char board[BOARD_SIZE][BOARD_SIZE];
	char turn='X';
	int r, c;
	int i, j;
	int count;
	int win;

	for (i=0; i<BOARD_SIZE; i++)
		for (j=0; j<BOARD_SIZE; j++)
			board[i][j]= ' ';
	count = 1;
	display(board);
	do
	{
		printf("Player %c(За ї­):", turn);
		scanf("%d %d", &r, &c);

		if (board[r][c]!=' ') continue;

		board[r][c] = turn;
		display(board);

		if (win=winCheck(board, r, c))
			printf("Player %c wins!\n", turn);
		if (turn=='X')
			turn = 'O';
		else
			turn = 'X';
		count++;
	} while (!win && count <= BOARD_SIZE * BOARD_SIZE);
	if (!win && count == BOARD_SIZE * BOARD_SIZE)
		printf("Nobody win!\n");
}