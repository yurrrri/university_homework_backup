#include <stdio.h>
#include <string.h>

#define MAX_VIDEO 100
#define MAX_CHAR 100 // 문자열의 max 문자

struct VideoInfo { // 재고 대장: 현재 보유하고 있는 Video 정보 저장
 char title[MAX_CHAR] ;
 int qty ; // 수량
};

int main(void)
{
	int videoCount = 5;
	int choice;
	int i;
	char title[MAX_CHAR];
	int qty;
	int rt=0;

	struct VideoInfo videoList[MAX_VIDEO];
	strcpy(videoList[0].title, "BeforeSunrise");
	videoList[0].qty = 1;
	strcpy(videoList[1].title, "BeforeSunset");
	videoList[1].qty = 3;
	strcpy(videoList[2].title, "BeforeMidnight");
	videoList[2].qty = 5;
	strcpy(videoList[3].title, "Casablanca");
	videoList[3].qty = 7;
	strcpy(videoList[4].title, "EdgeOfTomorrow");
	videoList[4].qty = 9;

	printf("1(All Video 출력), 2(구입), 3(검색), 4(종료): ");
	scanf("%d", &choice);
	while (choice != 4) {
		switch(choice) {
			case 1: // 보유 Video들을 출력
				printf("Video 제목\t 수량\n");
				printf("-----------------------\n");
				for (i=0; i<videoCount; i++)
					printf("%s	%d\n", videoList[i].title, videoList[i].qty);
				break;
			case 2: // Video 구입
				printf("Enter video 제목: ");
				scanf("%s", title);
				printf("Enter video 수량: ");
				scanf("%d", &qty);
				for (i=0; i<videoCount; i++);
				strcpy(videoList[i].title, title);
				videoList[i].qty = qty;
				videoCount++;
				break;
			case 3: // title 로 Video 찾기
				printf("Enter video 제목: ");
				scanf("%s", title);
				for (i=0; i<videoCount; i++){
					if (strcmp(videoList[i].title, title)==0)
						rt=1;
						break;
				}
				if (rt==1)
					printf("대여 가능합니다.\n");
				else
					printf("그런 비디오는 없습니다.\n");

				break;
 }
	printf("1(All Video 출력), 2(구입), 3(검색), 4(종료): ");
	scanf("%d", &choice);
	}
} 