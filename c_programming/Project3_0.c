#include <stdio.h>
#include <string.h>

#define MAX_VIDEO 100
#define MAX_CHAR 100 // ���ڿ��� max ����

struct VideoInfo { // ��� ����: ���� �����ϰ� �ִ� Video ���� ����
 char title[MAX_CHAR] ;
 int qty ; // ����
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

	printf("1(All Video ���), 2(����), 3(�˻�), 4(����): ");
	scanf("%d", &choice);
	while (choice != 4) {
		switch(choice) {
			case 1: // ���� Video���� ���
				printf("Video ����\t ����\n");
				printf("-----------------------\n");
				for (i=0; i<videoCount; i++)
					printf("%s	%d\n", videoList[i].title, videoList[i].qty);
				break;
			case 2: // Video ����
				printf("Enter video ����: ");
				scanf("%s", title);
				printf("Enter video ����: ");
				scanf("%d", &qty);
				for (i=0; i<videoCount; i++);
				strcpy(videoList[i].title, title);
				videoList[i].qty = qty;
				videoCount++;
				break;
			case 3: // title �� Video ã��
				printf("Enter video ����: ");
				scanf("%s", title);
				for (i=0; i<videoCount; i++){
					if (strcmp(videoList[i].title, title)==0)
						rt=1;
						break;
				}
				if (rt==1)
					printf("�뿩 �����մϴ�.\n");
				else
					printf("�׷� ������ �����ϴ�.\n");

				break;
 }
	printf("1(All Video ���), 2(����), 3(�˻�), 4(����): ");
	scanf("%d", &choice);
	}
} 