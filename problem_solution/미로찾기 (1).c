#include <stdio.h>
#define WIDTH 10
#define HEIGHT 10

int screen[WIDTH][HEIGHT] = { 
0, 0, 0,-1,-1,-1,-1,-1,-1,-1,
-1,-1, 0,-1,-1,-1,-1,-1,-1,-1,
-1, 0, 0, 0, 0, 0, 0,-1,-1,-1, 
-1,-1,-1,-1, 0,-1, 0,-1,-1,-1, 
-1,-1,-1,-1, 0,-1, 0,-1,-1,-1,
-1,-1, 0, 0, 0,-1, 0, 0, 0,-1,
-1,-1,-1,-1, 0,-1, 0,-1,-1,-1,
-1,-1,-1,-1, 0,-1, 0,-1, 0,-1,
-1,-1,-1,-1, 0,-1,-1,-1, 0,-1, 
-1,-1,-1,-1, 0, 0, 0, 0, 0, 0 };

void display() {
	for (int i = 0; i < WIDTH; i++) {
		for (int j = 0; j < HEIGHT; j++) {
			printf("%3d ", screen[i][j]);
		}
		printf("\n");
	}
	printf("\n");
}

void flood_fill(int x, int y) {

	static int count = 1;

	if (screen[x][y] == 0) {

		screen[x][y] = count++;

		if (y+1<WIDTH)
			flood_fill(x, y + 1); // 오른 쪽 3시
		if (x+1<HEIGHT)
			flood_fill(x + 1, y); // 아래 쪽 6시
		if (y-1>=0)
			flood_fill(x, y - 1); // 왼쪽 9시
		if (x-1>=0)
			flood_fill(x - 1, y); // 위쪽 12시
	}
}

int main(void) {

	printf("미로:\n");
	display();

	flood_fill(0, 0);
	
	printf("시작점을 <0 0>을 한 미로방문<순서표기>:\n");
	display();
}